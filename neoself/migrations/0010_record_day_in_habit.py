# Generated by Django 4.1.4 on 2022-12-13 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neoself', '0009_weeklog'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='day_in_habit',
            field=models.IntegerField(default=0),
        ),
    ]
