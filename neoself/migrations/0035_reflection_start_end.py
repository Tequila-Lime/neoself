# Generated by Django 4.1.4 on 2023-01-09 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neoself', '0034_record_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='reflection',
            name='start_end',
            field=models.BooleanField(default=True),
        ),
    ]