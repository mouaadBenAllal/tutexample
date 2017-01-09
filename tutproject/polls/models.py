from __future__ import unicode_literals
from django.conf import settings
import datetime

from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', null=True, blank=True, default=None)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class ToDo(models.Model):

    todo = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', null=True, blank=True, default=timezone.now,)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, )
    work = models.BooleanField('Done:', default=False)

    def __str__(self):
        return self.todo

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class UserProfile(models.Model):

    user = models.OneToOneField(User, default=False)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()
    user_image = models.FileField(upload_to='userimages/', default=False)

    def __str__(self):
        return self.name
