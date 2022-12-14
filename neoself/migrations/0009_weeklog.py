# Generated by Django 4.1.4 on 2022-12-13 18:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neoself', '0008_rename_name_questionnaire_habit_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeekLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('questionnaire', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='neoself.questionnaire')),
                ('records', models.ManyToManyField(to='neoself.record')),
                ('reflection', models.ManyToManyField(to='neoself.reflection')),
            ],
        ),
    ]
