# Generated by Django 4.1.4 on 2023-01-05 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neoself', '0029_rename_likes_num_record_comments_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='likes_num',
            field=models.IntegerField(default=0),
        ),
    ]