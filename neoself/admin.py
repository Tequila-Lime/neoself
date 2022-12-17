from django.contrib import admin
from .models import User,Questionnaire,Reflection,Record,Result,Notification,Friend,Badge,WeekLog,Reaction
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['id','username','full_name','bio','created_at', 'avatar']
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
admin.site.register(Reaction)