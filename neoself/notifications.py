
from .models import User,Questionnaire,Reflection,Record,Result,Notification,Friend,Badge,WeekLog 
import threading
import time
import datetime
from datetime import datetime, timedelta
from datetime import date


# this should run every day at 4 pm

def send_messages():
    for habit in Questionnaire.objects.filter(opt_in=True):
        dow = [habit.monday,habit.tuesday,habit.wednesday,habit.thursday,habit.friday,habit.saturday,habit.sunday]
        dow_num = []
        dow_count = 0
        for time in dow:
            if time == True:
                dow_num.append(dow_count)
            dow_count += 1
        if datetime.today().weekday() in dow_num:
            # this is where a message should send 
            print(f'Message to {habit.user.full_name} to fill out record for habit')
