from django.db import models
from datetime import datetime


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    # image = models.CharField(max_length=100)
    # likes = models.PositiveIntegerField(default=0)
    body = models.CharField(max_length=1000000)
    # created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
  

   






