# Generated by Django 4.1.4 on 2022-12-16 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neoself', '0020_reflection_notif_time_alter_notification_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='opt_in',
            field=models.BooleanField(default=False),
        ),
    ]