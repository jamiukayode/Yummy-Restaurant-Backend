# Generated by Django 5.0.6 on 2024-07-07 20:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subcode', '0009_booktable_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='booktable',
            name='datebooked',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='message',
            name='datemessage',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
