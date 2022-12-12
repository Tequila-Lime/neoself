from django.shortcuts import render
from .models import User,Questionnaire,Reflection,Record,Result,Notification,Friend,Badge  
from .serializers import UserSerializer,QuestionnaireSerializer,ReflectionSerializer,RecordSerializer,ResultSerializer,NotificationSerializer,FriendSerializer 
from rest_framework import generics, status, parsers
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q
from django.contrib.postgres.search import SearchVector,SearchQuery,SearchRank
from django.db import IntegrityError
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
    permission_classes = [IsAuthenticated]

class RecordView(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Record.objects.filter(week_reflection__questionnaire__user=self.request.user)
        return queryset
# Try to make a record view that seperates habit

class RecordDetail(generics.RetrieveUpdateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated]

class FriendDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Allows user to view friend detail as well as delete the relationship.
    '''
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    permission_classes = [IsAuthenticated]

class FriendHabitSearchView(generics.ListCreateAPIView):
    '''
    Allows user to search friends by habit
    '''
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Friend.objects.filter(friend_id__questionnaire__name=self.request.user)
        return queryset