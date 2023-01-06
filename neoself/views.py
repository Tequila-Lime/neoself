from django.shortcuts import render
from .models import User,Questionnaire,Reflection,Record,Result,Notification,Friend,Badge,WeekLog, Reaction, Like 
from .serializers import UserSerializer,QuestionnaireSerializer,ReflectionSerializer,RecordSerializer,WeekLogSerializer,ResultSerializer,NotificationSerializer,FriendSerializer, ReactionSerializer, FriendPostSerializer, ResultDetailSerializer, LikeSerializer
from rest_framework import generics, status, parsers, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from django.contrib.postgres.search import SearchVector,SearchQuery,SearchRank
from django.db import IntegrityError
from rest_framework.parsers import MultiPartParser, FormParser
from datetime import datetime, timedelta
import time
from datetime import date
# Create your views here.

class AllUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = User.objects.filter(username=self.request.user)
        return queryset

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

class UserSelfDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self):
        return self.request.user

class UserSearchList(generics.ListAPIView):
    model = User
    context_object_name = "quotes"
    serializer_class= UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        query = self.request.GET.get("q")
        return User.objects.annotate(search=SearchVector("username","full_name")).filter(
            search__icontains=query
        )

class QuestionnaireView(generics.ListCreateAPIView):
    '''
    Users can see all their habits they wanted to start
    '''
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Questionnaire.objects.filter(user=self.request.user).order_by('-date')
        return queryset

    def perform_create(self, serializer):
        #this is to POST a new Card
        serializer.save(user=self.request.user)

class QuestionnaireDetail(generics.RetrieveUpdateAPIView):
    '''
    Users should only be able to see the individual Questionnaire after they created it.
    Editing to this plan will be done in the weekly reflections 
    '''
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class RecordView(generics.ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        first = date(2000,5,17)
        today = date.today()
        queryset = Record.objects.filter(week_reflection__questionnaire__user=self.request.user, date__range=(first, today)).order_by('-date')
        return queryset
# Try to make a record view that seperates habit

class RecordAllView(generics.ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        first = date(2000,5,17)
        today = date.today()
        queryset = Record.objects.filter(Q(public=True,filled_in = True) & Q(date__range=(first, today)) & ~Q(user=self.request.user)).order_by('-date')
        return queryset

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

class UserRecordView(generics.ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        first = date(2000,5,17)
        today = date.today()
        user_id = self.kwargs['user_id']
        queryset = Record.objects.filter(week_reflection__questionnaire__user=user_id, date__range=(first, today), public=True, filled_in = True).order_by('-date') 
        return queryset

class RecordDetail(generics.RetrieveUpdateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class UserTodayRecordView(generics.ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Record.objects.filter(week_reflection__questionnaire__user=self.request.user, date=date.today())
        return queryset

class WeeklogRecordsView(generics.ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        wk_id = self.kwargs["wk_id"]
        weeklog = WeekLog.objects.get(id=wk_id)
        queryset = Record.objects.filter(id__in=weeklog.records.all()) 
        return queryset

class RecordHabitDetail(generics.ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        first = date(2000,5,17)
        today = date.today()
        questionnaire_id = self.kwargs['questionnaire_id']
        questionnaire = Questionnaire.objects.get(id=questionnaire_id)
        reflection = Reflection.objects.filter(questionnaire=questionnaire)
        queryset = Record.objects.filter(week_reflection__in=reflection, date__range=(first, today)).order_by('-date')
        return queryset

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

class ReflectionHabitView(generics.ListCreateAPIView):
    queryset = Reflection.objects.all()
    serializer_class = ReflectionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        questionnaire_id = self.kwargs['id']
        questionnaire = Questionnaire.objects.get(id=questionnaire_id)
        queryset = Reflection.objects.filter(questionnaire=questionnaire).order_by('-date')
        return queryset

    def perform_create(self, serializer):
        serializer.save(questionnaire=self.kwargs['id'])

class ReflectionDetail(generics.RetrieveAPIView):
    '''
    Allows user to view reflection detail. Eventually there should be a time constraint on when a user is able to update
    '''
    queryset = Reflection.objects.all()
    serializer_class = ReflectionSerializer
    permission_classes = [IsAuthenticated] 

class FriendView(generics.ListCreateAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    permission_classes = []

    def get_queryset(self):
        queryset = Friend.objects.filter(Q(current_user=self.request.user.id) | Q(friend=self.request.user))
        return queryset

    def perform_create(self, serializer):
        serializer.save(current_user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return FriendPostSerializer
        return self.serializer_class

class FriendAllView(generics.ListAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class FriendSearchView(generics.ListCreateAPIView):
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

class QuestionnaireWeeklogsView(generics.ListAPIView):
    queryset = WeekLog.objects.all()
    serializer_class=WeekLogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        first = date(2000,5,17)
        today = date.today()
        queryset = WeekLog.objects.filter(questionnaire=self.kwargs["questionnaire_id"], date__range=(first, today)).order_by('-date')
        return queryset

class WeekLogDetail(generics.RetrieveAPIView):
    queryset = WeekLog.objects.all()
    serializer_class = WeekLogSerializer
    permission_classes = [IsAuthenticated]

class ResultsView(generics.ListAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Result.objects.filter(questionnaire__user=self.request.user)
        return queryset

class QuestionnaireResultView(generics.ListAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Result.objects.filter(questionnaire=self.kwargs["questionnaire_id"])
        return queryset

class ResultsAllView(generics.ListAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = []

class ResultsDetail(generics.RetrieveAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class UserAvatarView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser, FormParser)

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

    def perform_create(self, serializer):
        #this is to POST a new Card
        serializer.save(commentor=self.request.user)

class RecordReactionView(generics.ListCreateAPIView):
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer
    permission_classes = []

    def get_queryset(self):
        record_id = self.kwargs["record_id"]
        queryset = Reaction.objects.filter(record=record_id)
        return queryset

    def perform_create(self, serializer):
        #this is to POST a new Card
        serializer.save(commentor=self.request.user)

class ReactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class RecordLikeView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = []

    def get_queryset(self):
        record_id = self.kwargs["record_id"]
        queryset = Like.objects.filter(record=record_id, person_liked=self.request.user)
        return queryset

    def perform_create(self, serializer):
        #this is to POST a new Card
        serializer.save(person_liked=self.request.user)

class RecordLikeDetail(generics.RetrieveDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = []