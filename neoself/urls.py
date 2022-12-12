from django.urls import path, include
from . import views

urlpatterns = [
    path('user/', views.UserView.as_view(), name='user-profile'),
    path('user/self/', views.UserDetail.as_view(), name='user-detail'),
    path('questionnaire/', views.QuestionnaireView.as_view(), name='habit-questionnaire'),
    path('questionnaire/<int:pk>/',views.QuestionnaireDetail.as_view(), name='specific-habit-questionnaire'),
    path('reflection/', views.ReflectionView.as_view(), name="reflection"),
    path('reflection/<int:pk>/', views.ReflectionDetail.as_view(), name=('reflection-detail')),
    path('friends', views.FriendView.as_view(), name="friend"),
    path('friends/<int:pk>/', views.FriendDetail.as_view(), name="friend-detail"),
    path('friends/search/', views.FriendHabitSearchView.as_view(), name="friend-search")
]
