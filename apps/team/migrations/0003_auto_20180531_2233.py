# Generated by Django 2.0.5 on 2018-05-31 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('team', '0002_coach_perms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coach',
            name='perms',
        ),
        migrations.AddField(
            model_name='coach',
            name='perms',
            field=models.ManyToManyField(to='auth.Permission'),
        ),
    ]
