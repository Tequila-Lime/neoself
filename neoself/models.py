from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.db.models.signals import post_save
from django.shortcuts import get_object_or_404
from django.dispatch import receiver
import datetime

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    full_name = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Questionnaire(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    start_habit = models.BooleanField(default=True)
    habit_name = models.CharField(max_length=200)
    date = models.DateField(default=date.today)
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
    start_today = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} habit is {self.habit_name}"

class Reflection(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, null=True, blank=True)
    cue_question_1 = models.TextField(max_length=1000)
    cue_question_2 = models.TextField(max_length=1000)
    cue_question_3 = models.TextField(max_length=1000)
    craving_question_1 = models.TextField(max_length=1000)
    response_question_1 = models.TextField(max_length=1000)
    response_question_2 = models.TextField(max_length=1000)
    goal_metric = models.IntegerField(default=0)
    date = models.DateField(default=date.today)

    def __str__(self):
        return f"reflection on {self.questionnaire} on {self.date}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['date', 'questionnaire'], name='unique_reflection')
        ]

class Record(models.Model):
    week_reflection = models.ForeignKey(Reflection, on_delete=models.CASCADE, null=True, blank=True)
    daily_record = models.IntegerField(default=0)
    cue_dh = models.BooleanField(default=False)
    craving_dh = models.BooleanField(default=False)
    response_dh = models.BooleanField(default=False)
    comment_dh = models.TextField(max_length=1000)
    day_in_habit = models.IntegerField(default=0)
    date = models.DateField(default=date.today)

    def __str__(self):
        return f"record for {self.week_reflection}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['date', 'week_reflection'], name='unique_record')
        ]

# A model that gets all the data for the week so we can give a summary
class WeekLog(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, null=True, blank=True)
    reflection = models.ManyToManyField(Reflection)
    records = models.ManyToManyField(Record)
    date = models.DateField(default=date.today)

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

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['current_user', 'friend'], name='unique_friendship')
        ]

class Badge (models.Model):
    pass

@receiver(post_save, sender=Questionnaire)
def save_reflection(sender,instance,created, *args, **kwargs):
    if created:
        Reflection.objects.create(
            questionnaire = instance,
            cue_question_1 = instance.cue_question_1,
            cue_question_2 = instance.cue_question_2,
            cue_question_3 = instance.cue_question_3,
            craving_question_1 = instance.craving_question_1,
            response_question_1 = instance.response_question_1,
            response_question_2 = instance.response_question_2,
            goal_metric = instance.goal_metric,
            date = instance.date
        )
        instance.save()
#need day_in_habit to be determined by the date and auto generated
# Need all records for a particular habit to be made in a week to automatically be put together to make a week summary 