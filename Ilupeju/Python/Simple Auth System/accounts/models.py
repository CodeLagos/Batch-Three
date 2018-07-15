from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    username = models.CharField(max_length=100, default='smith')
    phone = models.IntegerField(default=0)




