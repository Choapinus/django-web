# Generated by Django 2.0.5 on 2018-05-31 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='perms',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.Permission'),
            preserve_default=False,
        ),
    ]
