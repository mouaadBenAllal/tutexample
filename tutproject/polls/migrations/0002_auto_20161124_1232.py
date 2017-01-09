# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-24 12:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='date published'),
        ),
    ]
