from django.contrib import admin
from .models import User,Questionnaire,Reflection,Record,Result,Notification,Friend,Badge, WeekLog
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Questionnaire)
admin.site.register(Reflection)
admin.site.register(Record)
admin.site.register(Result)
admin.site.register(Notification)
admin.site.register(Friend)
admin.site.register(Badge)
admin.site.register(WeekLog)