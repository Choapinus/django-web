# Generated by Django 2.0.5 on 2018-05-26 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_auto_20180526_0300'),
        ('team', '0004_coach_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customcoach',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='CustomCoach',
        ),
    ]
