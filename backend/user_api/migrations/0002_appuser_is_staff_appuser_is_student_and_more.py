# Generated by Django 5.0.6 on 2024-07-22 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='appuser',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='appuser',
            name='is_teacher',
            field=models.BooleanField(default=False),
        ),
    ]
