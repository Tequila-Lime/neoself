from rest_framework import serializers
from .models import User,Questionnaire,Reflection,Record,Result,Notification,Friend,Badge,WeekLog, Reaction

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id','username','full_name','bio','created_at', 'avatar')

    def update(self, instance, validated_data):
        if "file" in self.initial_data:
            file = self.initial_data.get("file")
            instance.avatar.save(file.name, file, save=True)
            return instance
        # this call to super is to make sure that update still works for other fields
        return super().update(instance, validated_data)
        
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
        fields = ('id','week_reflection','daily_record','cue_dh','craving_dh','response_dh','comment_dh','date','public','filled_in','likes_num')

class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        fields = ('id','questionnaire','habit_log','success')

class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = ('id','habit','time','message')

class FriendSerializer(serializers.ModelSerializer):
    friend = serializers.SlugRelatedField(slug_field='username', read_only=True)
    class Meta:
        model = Friend
        fields = ('id','friend','created_at')

# class FriendSearchSerializer(serializers.ModelSerializer):
#     friend= serializers.SerializerMethodField()
    
#     class Meta:
#         model = User
#         fields = ('friend','username','full_name')

class WeekLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeekLog
        fields = '__all__'

class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = '__all__'
