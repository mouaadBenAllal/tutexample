# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20161208_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_image',
            field=models.FileField(default=False, upload_to='images/userimages/'),
        ),
    ]