# Generated by Django 4.1.4 on 2022-12-11 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neoself', '0003_rename_response_question_1_questionnaire_response_question_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reflection',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
