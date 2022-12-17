# Generated by Django 4.1.4 on 2022-12-17 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neoself', '0021_alter_questionnaire_opt_in'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='likes_num',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neoself.record')),
            ],
        ),
    ]
