# Generated by Django 3.0.8 on 2020-12-20 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='interests',
            field=models.CharField(default='None', max_length=150),
        ),
        migrations.AddField(
            model_name='profile',
            name='roll_no',
            field=models.CharField(default='None', max_length=9),
        ),
        migrations.AddField(
            model_name='profile',
            name='room_no',
            field=models.IntegerField(default='0'),
        ),
    ]
