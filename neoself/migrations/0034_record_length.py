# Generated by Django 4.1.4 on 2023-01-07 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neoself', '0033_like_unique_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='length',
            field=models.IntegerField(default=0),
        ),
    ]
