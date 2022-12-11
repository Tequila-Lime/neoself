from django.urls import path, include
from . import views

urlpatterns = [
    path('user/', views.UserView.as_view(), name='user-profile'),
    path('user/self/', views.UserDetail.as_view(), name='user-detail'),
    path('questionnaire/', views.QuestionnaireView.as_view(), name='habit-questionnaire'),
    path('questionnaire/<int:pk>/',views.QuestionnaireDetail.as_view(), name='specific-habit-questionnaire'),

]
