from django.shortcuts import render
from .models import User,Questionnaire,Reflection,Record,Result,Notification,Friend,Badge,WeekLog, Reaction 
from .serializers import UserSerializer,QuestionnaireSerializer,ReflectionSerializer,RecordSerializer,WeekLogSerializer,ResultSerializer,NotificationSerializer,FriendSerializer, ReactionSerializer
from rest_framework import generics, status, parsers, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from django.contrib.postgres.search import SearchVector,SearchQuery,SearchRank
from django.db import IntegrityError
import datetime
from datetime import datetime, timedelta
import time
from datetime import date
# Create your views here.

class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = User.objects.filter(username=self.request.user)
        return queryset

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class UserSearchList(generics.ListAPIView):
    model = User
    context_object_name = "quotes"
    serializer_class= UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        query = self.request.GET.get("q")
        return User.objects.annotate(search=SearchVector("username","first_name","last_name")).filter(
            search=query
        )

class QuestionnaireView(generics.ListCreateAPIView):
    '''
    Users can see all their habits they wanted to start
    '''
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Questionnaire.objects.filter(user=self.request.user)
        return queryset

class QuestionnaireDetail(generics.RetrieveAPIView):
    '''
    Users should only be able to see the individual Questionnaire after they created it.
    Editing to this plan will be done in the weekly reflections 
    '''
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class RecordView(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        first = date(2000,5,17)
        today = date.today()
        queryset = Record.objects.filter(week_reflection__questionnaire__user=self.request.user, date__range=(first, today)).order_by('-date')
        return queryset
# Try to make a record view that seperates habit

class FriendRecordView(generics.ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        friends = Friend.objects.filter(Q(current_user=self.request.user) | Q(friend=self.request.user))
        people = []
        for friend in friends:
            if friend.current_user == self.request.user:
                people.append(friend.friend)
            else:
                people.append(friend.current_user)
        first = date(2000,5,17)
        today = date.today()
        queryset = Record.objects.filter(week_reflection__questionnaire__user__in=people, date__range=(first, today), public=True, filled_in=True).order_by('-date')
        return queryset

class RecordDetail(generics.RetrieveUpdateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ReflectionView(generics.ListCreateAPIView):
    '''
    These are based on questionnaire model and the data should eventually be populated by it initially
    '''
    queryset = Reflection.objects.all()
    serializer_class = ReflectionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Reflection.objects.filter(questionnaire__user=self.request.user)
        return queryset

class ReflectionDetail(generics.RetrieveUpdateAPIView):
    '''
    Allows user to view reflection detail. Eventually there should be a time constraint on when a user is able to update
    '''
    queryset = Reflection.objects.all()
    serializer_class = ReflectionSerializer
    permission_classes = [IsAuthenticated] 

class FriendView(generics.ListCreateAPIView):
    '''
    Allows user to view friends list as well as add an a new friend.
    '''
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    ordering_fields = ['created_at']
    search_fields = ['friend']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Friend.objects.filter(current_user=self.request.user.pk)
        return queryset
    def perform_create(self, serializer):
        serializer.save(current_user=self.request.user)
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            error_data = {
                "error": "You are already following this user."
            }
            return Response(error_data, status=status.HTTP_400_BAD_REQUEST)

class FriendDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    permission_classes = [IsAuthenticated]
    
class WeekLogView(generics.ListAPIView):
    queryset = WeekLog.objects.all()
    serializer_class = WeekLogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        first = date(2000,5,17)
        today = date.today()
        queryset = WeekLog.objects.filter(questionnaire__user=self.request.user, date__range=(first, today)).order_by('-date')
        return queryset

class ResultsView(generics.ListAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Result.objects.filter(questionnaire__user=self.request.user)
        return queryset

class ResultsDetail(generics.RetrieveAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class UserAvatarView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = [parsers.FileUploadParser]

    def get_object(self):
        #return User.objects.first()
        return self.request.user
    
    def get_parsers(self):
        if self.request.FILES:
            self.parser_classes.append(parsers.FileUploadParser)
        return [parser() for parser in self.parser_classes]

class ReactionView(generics.ListCreateAPIView):
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer
    permission_classes = []

class ReactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
