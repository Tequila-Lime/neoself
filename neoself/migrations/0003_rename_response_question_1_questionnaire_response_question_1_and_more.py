# Generated by Django 4.1.4 on 2022-12-10 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neoself', '0002_badge_questionnaire_record_result_reflection_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionnaire',
            old_name='Response_question_1',
            new_name='response_question_1',
        ),
        migrations.RenameField(
            model_name='questionnaire',
            old_name='Response_question_2',
            new_name='response_question_2',
        ),
        migrations.RenameField(
            model_name='reflection',
            old_name='Response_question_1',
            new_name='response_question_1',
        ),
        migrations.RenameField(
            model_name='reflection',
            old_name='Response_question_2',
            new_name='response_question_2',
        ),
    ]