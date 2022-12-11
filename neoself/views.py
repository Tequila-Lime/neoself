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