# Generated by Django 4.1.4 on 2022-12-14 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neoself', '0017_remove_weeklog_reflection'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='questionnaire',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='neoself.questionnaire'),
        ),
    ]
