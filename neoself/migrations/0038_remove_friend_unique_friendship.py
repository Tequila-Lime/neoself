# Generated by Django 4.1.4 on 2023-01-10 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neoself', '0037_reflection_name'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='friend',
            name='unique_friendship',
        ),
    ]