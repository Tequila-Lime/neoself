# Generated by Django 4.1.4 on 2023-01-05 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neoself', '0030_record_likes_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
