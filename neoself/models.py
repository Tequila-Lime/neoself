from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    full_name = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Questionnaire(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    start_end = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField(default=30)
    metric_label = models.CharField(max_length=50)
    metric_baseline = models.IntegerField(default=0)
    goal_label = models.CharField(max_length=50)
    goal_metric = models.IntegerField(default=0)
    opt_in = models.BooleanField(default=True)
    cue_question_1 = models.TextField(max_length=1000)
    cue_question_2 = models.TextField(max_length=1000)
    cue_question_3 = models.TextField(max_length=1000)
    craving_question_1 = models.TextField(max_length=1000)
    response_question_1 = models.TextField(max_length=1000)
    response_question_2 = models.TextField(max_length=1000)
    signature = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user} habit is {self.name}"

class Reflection(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, null=True, blank=True)
    cue_question_1 = models.TextField(max_length=1000)
    cue_question_2 = models.TextField(max_length=1000)
    cue_question_3 = models.TextField(max_length=1000)
    craving_question_1 = models.TextField(max_length=1000)
    response_question_1 = models.TextField(max_length=1000)
    response_question_2 = models.TextField(max_length=1000)
    goal_metric = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"reflection on {self.questionnaire}"

class Record(models.Model):
    week_reflection = models.ForeignKey(Reflection, on_delete=models.CASCADE, null=True, blank=True)
    daily_record = models.IntegerField(default=0)
    cue_dh = models.BooleanField(default=False)
    craving_dh = models.BooleanField(default=False)
    response_dh = models.BooleanField(default=False)
    comment_dh = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"record for {self.week_reflection}"

class Result(models.Model):
    habit_log = models.ManyToManyField(Record)
    success = models.BooleanField(default=False)

class Notification(models.Model):
    habit = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, null=True, blank=True)
    time = models.CharField(max_length=50)
    message = models.CharField(max_length=300)

    def __str__(self):
        return f"notification for {self.habit}"

class Friend(models.Model):
    current_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='current_user')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendships')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    best_friend = models.BooleanField(default='False')

    def __str__(self):
        return f"{self.current_user} is friends with {self.friend}"

class Badge (models.Model):
    pass
