from rest_framework import serializers
from .models import User,Like,Questionnaire,Reflection,Record,Result,Notification,Friend,Badge,WeekLog, Reaction

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id','username','full_name','bio','created_at', 'avatar')

    def update(self, instance, validated_data):
        if "file" in self.initial_data:
            file = self.initial_data.get("file")
            instance.avatar.save(file.name, file, save=True)
            return instance
        if 'avatar' in validated_data:
            avatar = validated_data.get('avatar')
            instance.avatar.save(avatar.name, avatar, save=True)
        # this call to super is to make sure that update still works for other fields
        return super().update(instance, validated_data)
        
class QuestionnaireSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questionnaire
        fields = ('id','public','status','user','start_habit','habit_name','date','start_today','duration','sunday','monday','tuesday','wednesday','thursday','friday','saturday','metric_label','metric_baseline','goal_label','goal_metric','opt_in','cue_question_1','cue_question_2','cue_question_3','craving_question_1','response_question_1',    'response_question_2','signature' )

class ReflectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reflection
        fields = ('id','name','start_end','questionnaire','cue_question_1','cue_question_2','cue_question_3','craving_question_1','response_question_1','response_question_2','date', 'metric_baseline','goal_metric','metric_label')

class RecordSerializer(serializers.ModelSerializer):
    user_number = serializers.PrimaryKeyRelatedField(source='user', read_only=True)
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Record
        fields = ('id','user_number','length','user','week_reflection','daily_record','metric_label','cue_dh','craving_dh','response_dh','comment_dh','date','public','filled_in','likes_num','comments_num','habit_name', 'metric_label')

class RecordDataSerializer(serializers.ModelSerializer):
    user_number = serializers.PrimaryKeyRelatedField(source='user', read_only=True)
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    week_reflection = ReflectionSerializer(read_only=True)

    class Meta:
        model = Record
        fields = ('id','user_number','day_in_habit','length','user','week_reflection','daily_record','metric_label','cue_dh','craving_dh','response_dh','comment_dh','date','public','filled_in','likes_num','comments_num','habit_name', 'metric_label')

class ResultSerializer(serializers.ModelSerializer):
    questionnaire = serializers.SlugRelatedField(slug_field='habit_name', read_only=True)

    class Meta:
        model = Result
        fields = ('id','questionnaire','habit_log','success')

class ResultDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('id','questionnaire','habit_log','success')

class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = ('id','habit','time','message')

class FriendSerializer(serializers.ModelSerializer):
    friend_number = serializers.PrimaryKeyRelatedField(source='friend', read_only=True)
    current_number = serializers.PrimaryKeyRelatedField(source='current_user', read_only=True)
    friend = serializers.SlugRelatedField(slug_field='username', read_only=True)
    current_user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    
    class Meta:
        model = Friend
        fields = ('id','friend','friend_number','current_number','created_at','current_user')

class FriendPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = '__all__'

# class FriendSearchSerializer(serializers.ModelSerializer):
#     friend= serializers.SerializerMethodField()
    
#     class Meta:
#         model = User
#         fields = ('friend','username','full_name')

class WeekLogSerializer(serializers.ModelSerializer):
    questionnaire = serializers.SlugRelatedField(slug_field='habit_name', read_only=True)

    class Meta:
        model = WeekLog
        fields = '__all__'

class ReactionSerializer(serializers.ModelSerializer):
    commentor = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Reaction
        fields = ('id','record','commentor','gif_url')

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id','record','person_liked')
