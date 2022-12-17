from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('user/', views.UserView.as_view(), name='user-profile'),
    path('user/self/', views.UserDetail.as_view(), name='user-detail'),
    path('questionnaire/', views.QuestionnaireView.as_view(), name='habit-questionnaire'),
    path('questionnaire/<int:pk>/',views.QuestionnaireDetail.as_view(), name='specific-habit-questionnaire'),
    path('reflection/', views.ReflectionView.as_view(), name="reflection"),
    path('reflection/<int:pk>/', views.ReflectionDetail.as_view(), name=('reflection-detail')),
    path('friends/', views.FriendView.as_view(), name="friend"),
    path('friends/<int:pk>/', views.FriendDetail.as_view(), name="friend-detail"),
    path('friends/search/', views.FriendSearchView.as_view(), name="friend-search"),
    path('record/user/', views.RecordView.as_view(), name='user-records'),
    path('record/<int:pk>/', views.RecordDetail.as_view(), name='record-detail'),
    path('record/friends/', views.FriendRecordView.as_view(), name='friends-record'),
    path('weeklogs/', views.WeekLogView.as_view(), name="week-logs"),
    path('results/', views.ResultsView.as_view(), name='results'),
    path('results/<int:pk>/',views.ResultsDetail.as_view(), name="results-detail"),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)