# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20161208_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_image',
            field=models.FileField(default=False, upload_to='userimages/'),
        ),
    ]
