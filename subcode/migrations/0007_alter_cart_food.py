# Generated by Django 5.0.6 on 2024-06-25 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subcode', '0006_alter_user_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subcode.food'),
        ),
    ]