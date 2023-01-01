from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('user/', views.UserView.as_view(), name='user-profile'),
    path('user/all/', views.AllUserView.as_view(), name='all-users'),
    path('user/self/', views.UserDetail.as_view(), name='user-detail'),
    path('user/search/', views.UserSearchList.as_view(), name="user-search"),
    path('auth/users/me/avatar/', views.UserAvatarView.as_view(), name='user_avatar'),
    path('questionnaire/', views.QuestionnaireView.as_view(), name='habit-questionnaire'),
    path('questionnaire/<int:pk>/',views.QuestionnaireDetail.as_view(), name='specific-habit-questionnaire'),
    path('reflection/', views.ReflectionView.as_view(), name="reflection"),
    path('questionnaire/<int:id>/reflection/', views.ReflectionHabitView.as_view(), name='reflection-questionnaire'),
    path('reflection/<int:pk>/', views.ReflectionDetail.as_view(), name=('reflection-detail')),
    path('friends/', views.FriendView.as_view(), name="friend"),
    path('friends/all/', views.FriendAllView.as_view(), name="friend-all"),
    path('friends/<int:pk>/', views.FriendDetail.as_view(), name="friend-detail"),
    path('habit/<int:questionnaire_id>/records/', views.RecordHabitDetail.as_view(), name="Habit-records"),
    path('record/user/', views.RecordView.as_view(), name='user-records'),
    path('record/all/', views.RecordAllView.as_view(), name="all-records"),
    path('record/<int:pk>/', views.RecordDetail.as_view(), name='record-detail'),
    path('record/friends/', views.FriendRecordView.as_view(), name='friends-record'),
    path('record/today/user/', views.UserTodayRecordView.as_view(), name="today-user-records"),
    path('record/weeklog/<int:wk_id>/',views.WeeklogRecordsView.as_view(), name='weeklog-records'),
    path('record/user/<int:user_id>/',views.UserRecordView.as_view(), name="user-records"),
    path('weeklogs/', views.WeekLogView.as_view(), name="week-logs"),
    path('weeklogs/habit/<int:questionnaire_id>/', views.QuestionnaireWeeklogsView.as_view(), name="habit-weeklogs"),
    path('weeklogs/<int:pk>/', views.WeekLogDetail.as_view(), name="weeklog-details"),
    path('results/', views.ResultsView.as_view(), name='results'),
    path('results/all/', views.ResultsAllView.as_view(), name="results-all"),
    path('results/habit/<int:questionnaire_id>/', views.QuestionnaireResultView.as_view(),name="habit-result"),
    path('results/<int:pk>/',views.ResultsDetail.as_view(), name="results-detail"),
    path('reaction/',views.ReactionView.as_view(), name='record-reactions'),
    path('reaction/record/<int:record_id>/', views.RecordReactionView.as_view(), name="record-reaction"),
    path('reaction/<int:pk>/', views.ReactionDetail.as_view(), name='reaction-detail'),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)