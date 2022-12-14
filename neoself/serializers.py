from rest_framework import serializers
from .models import User,Questionnaire,Reflection,Record,Result,Notification,Friend,Badge  

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id','username','full_name','bio','created_at', 'avatar')

class QuestionnaireSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questionnaire
        fields = ('id','user','start_habit','habit_name','date','duration','metric_label','metric_baseline','goal_label','goal_metric','opt_in','cue_question_1','cue_question_2','cue_question_3','craving_question_1','response_question_1',    'response_question_2','signature' )

class ReflectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reflection
        fields = ('id','questionnaire','cue_question_1','cue_question_2','cue_question_3','craving_question_1','response_question_1','response_question_2','date')

class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = ('id','week_reflection','daily_record','cue_dh','craving_dh','response_dh','comment_dh','date','public','filled_in')

class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        fields = ('id','habit_log','success')

class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = ('id','habit','time','message')

class FriendSerializer(serializers.ModelSerializer):

    class Meta:
        model = Friend
        fields = ('id','current_user','friend','created_at')