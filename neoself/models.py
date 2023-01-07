from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.db.models.signals import post_save, pre_delete
from django.shortcuts import get_object_or_404
from django.dispatch import receiver
import datetime
from datetime import datetime, timedelta
import time
from django.db.models import Q

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    full_name = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to="user_avatars", blank=True, null=True)

    def __str__(self):
        return self.username

class Questionnaire(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    start_habit = models.BooleanField(default=True)
    habit_name = models.CharField(max_length=200)
    date = models.DateField(default=date.today)

    sunday = models.BooleanField(default=True)
    monday = models.BooleanField(default=True)
    tuesday = models.BooleanField(default=True)
    wednesday = models.BooleanField(default=True)
    thursday = models.BooleanField(default=True)
    friday = models.BooleanField(default=True)
    saturday = models.BooleanField(default=True)

    duration = models.IntegerField(default=30)
    metric_label = models.CharField(max_length=50)
    metric_baseline = models.IntegerField(default=0)
    goal_label = models.CharField(max_length=50)
    goal_metric = models.IntegerField(default=0)
    opt_in = models.BooleanField(default=False)
    cue_question_1 = models.TextField(max_length=1000)
    cue_question_2 = models.TextField(max_length=1000)
    cue_question_3 = models.TextField(max_length=1000)
    craving_question_1 = models.TextField(max_length=1000)
    response_question_1 = models.TextField(max_length=1000)
    response_question_2 = models.TextField(max_length=1000)
    signature = models.CharField(max_length=100)
    start_today = models.BooleanField(default=False)

    public=models.BooleanField(default=True)
    status = models.BooleanField(default=True)

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
    metric_baseline = models.IntegerField(default=0)
    goal_metric = models.IntegerField(default=0)
    metric_label = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField(default=date.today)
    notif_time = models.TimeField(null=True, blank=True) 

    def __str__(self):
        return f"reflection on {self.questionnaire} on {self.date}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['date', 'questionnaire'], name='unique_reflection')
        ]

class Record(models.Model):
    week_reflection = models.ForeignKey(Reflection, on_delete=models.CASCADE, null=True, blank=True)
    daily_record = models.IntegerField(default=0)
    habit_name= models.CharField(max_length=200,blank=True,null=True)
    metric_label = models.CharField(max_length=200,blank=True,null=True)
    cue_dh = models.BooleanField(default=False)
    craving_dh = models.BooleanField(default=False)
    response_dh = models.BooleanField(default=False)
    comment_dh = models.TextField(max_length=1000)
    day_in_habit = models.IntegerField(default=0)
    date = models.DateField(default=date.today)
    filled_in = models.BooleanField(default=False)
    public = models.BooleanField(default=True)
    comments_num = models.IntegerField(default=0)
    likes_num = models.IntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    length = models.IntegerField(default=0)

    def __str__(self):
        return f"record on {self.date} for {self.week_reflection}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['date', 'week_reflection'], name='unique_record')
        ]

class Reaction(models.Model):
    record=models.ForeignKey(Record, on_delete=models.CASCADE)
    commentor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    gif_url = models.CharField(max_length=500,blank=True, null=True) 

    def __str__(self):
        return f"{self.commentor.full_name} liked {self.record.week_reflection.questionnaire.habit_name} record"

class Like(models.Model):
    record=models.ForeignKey(Record, on_delete=models.CASCADE)
    person_liked = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['record', 'person_liked'], name='unique_like')
        ]

    def __str__(self):
        return f"{self.person_liked.full_name} liked {self.record.week_reflection.questionnaire.habit_name} record"


# A model that gets all the data for the week so we can give a summary
class WeekLog(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, null=True, blank=True)
    records = models.ManyToManyField(Record)
    date = models.DateField(default=date.today)
    day = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.questionnaire.user} {self.questionnaire.habit_name} on {self.date}"

class Result(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, null=True, blank=True)
    habit_log = models.ManyToManyField(Record)
    success = models.BooleanField(default=False)

    def __str__(self):
        return f"Result for {self.questionnaire.user} habit {self.questionnaire.habit_name}"

class Notification(models.Model):
    habit = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, null=True, blank=True)
    time = models.TimeField(null=True,blank=True)
    message = models.CharField(max_length=300)

    def __str__(self):
        return f"notification for {self.habit}"

class Friend(models.Model):
    current_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='current_user')
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
            metric_baseline = instance.metric_baseline,
            goal_metric = instance.goal_metric,
            metric_label=instance.metric_label,
            date = instance.date
        )
        loops = round(instance.duration / 7)
        if instance.start_today == True:
            wk_check = instance.date - timedelta(days=1)
        else:
            wk_check = instance.date
        num = 7
        for x in range(loops):
            #  + timedelta(days=7)
            WeekLog.objects.create(
                questionnaire = instance,
                date = wk_check + timedelta(days=7),
                day = num
            ) 
            wk_check += timedelta(days=7)
            num += 7
        Result.objects.create(
            questionnaire = instance,
        )
        if instance.opt_in == True:
            Notification.objects.create(
                habit = instance,
                message = f"Make sure to {instance.habit_name} today"
            )
        instance.save()
    elif not created:
        if instance.status == False:
            today = date.today()
            records = Record.objects.filter(week_reflection__questionnaire__id=instance.id,date__gt=today )
            records.delete()
        else:
            today = date.today()
            records = Record.objects.filter(week_reflection__questionnaire__id=instance.id,date__gt=today).update(public=instance.public, length=instance.duration)
            records = Record.objects.filter(week_reflection__questionnaire__id=instance.id).update(length=instance.duration)

#need day_in_habit to be determined by the date and auto generated
@receiver(post_save, sender=Reflection)
def all_habit_records(sender, instance, created, *args, **kwargs):  
    if created:
        questionnaire = Questionnaire.objects.get(id=instance.questionnaire.id)
        count = 0
        added_day = timedelta(days=1)
        # when to start counting records
        if questionnaire.start_today == True:
            reflection_day = instance.date - added_day
        else: 
            reflection_day = instance.date 
        d1 = datetime.strptime(f"{instance.date}", "%Y-%m-%d")
        d2 = datetime.strptime(f"{questionnaire.date}", "%Y-%m-%d")
        difference = d1-d2
        amount = questionnaire.duration-difference.days
        # determines day of week
        dow = [questionnaire.monday,questionnaire.tuesday,questionnaire.wednesday,questionnaire.thursday,questionnaire.friday,questionnaire.saturday,questionnaire.sunday]
        dow_num = []
        dow_count = 0
        for time in dow:
            if time == True:
                dow_num.append(dow_count)
            dow_count += 1
        for x in range(amount): 
            if difference.days == 0:
                weekday_eval = reflection_day + added_day 
                if weekday_eval.weekday() in dow_num:
                    Record.objects.create(
                        week_reflection = instance,
                        daily_record = 0,
                        cue_dh = False,
                        craving_dh = False,
                        response_dh = False,
                        comment_dh = False,
                        day_in_habit = count + 1,
                        date = reflection_day + added_day,
                        public = questionnaire.public,
                        user = questionnaire.user,
                        metric_label = questionnaire.metric_label,
                        habit_name = questionnaire.habit_name,
                        length = questionnaire.duration
                    )
            else:
                records = Record.objects.filter(week_reflection__questionnaire__id=questionnaire.id, date=reflection_day + added_day)
                ids =[]
                for record in records:
                    ids.append(record.id)
                Record.objects.filter(id__in=ids).update(week_reflection=instance)
            
            added_day+=timedelta(days=1)
            count+=1
        Notification.objects.filter(habit=instance.questionnaire).update(
            time=instance.notif_time
        )
        instance.save()

@receiver(post_save, sender=Record)
def record_filled_in(sender, instance, created, *args, **kwargs):
    if not created:
        Record.objects.filter(pk=instance.pk).update(filled_in=True)

# Need all records for a particular habit to be made in a week to automatically be put together to make a week summary 
@receiver(post_save, sender=WeekLog)
def week_logs(sender, instance, created, *args, **kwargs):
    if created:
        top = instance.date
        bottom =instance.date - timedelta(days=6)
        records = Record.objects.filter(week_reflection__questionnaire = instance.questionnaire,
        date__range=(bottom,top) )
        object = WeekLog.objects.get(id=instance.id)
        for record in records:
            object.records.add(record)

@receiver(post_save, sender=Result)
def result_logs(sender, instance, created, *args, **kwargs):
    if created:
        records = Record.objects.filter(week_reflection__questionnaire = instance.questionnaire)
        object = Result.objects.get(id=instance.id)
        for record in records:
            object.habit_log.add(record)

@receiver(post_save, sender=Notification)
def reflect_get_alert_time(sender, instance, created, *args, **kwargs):
    if not created:
        Reflection.objects.filter(questionnaire=instance.habit).update(
            notif_time= instance.time
        )

@receiver(post_save, sender=Reaction)
def add_like_count(sender,instance,created,*args,**kwargs):
    if created:
        likes = Record.objects.get(id=instance.record.id)
        Record.objects.filter(id=instance.record.id).update(
            comments_num = likes.comments_num + 1
        )

@receiver(pre_delete, sender=Reaction)
def subtract_like_count(sender, instance, using, *args, **kwargs):
    likes = Record.objects.get(id=instance.record.id)
    Record.objects.filter(id=instance.record.id).update(
        comments_num = likes.comments_num - 1
    )

