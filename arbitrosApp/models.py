# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username

class Videos(models.Model):
    path = models.TextField(default='.')
    video = models.FileField()
    name = models.TextField(default='a')