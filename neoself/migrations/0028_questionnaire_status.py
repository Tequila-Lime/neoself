# Generated by Django 4.1.4 on 2023-01-05 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neoself', '0027_reflection_metric_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
