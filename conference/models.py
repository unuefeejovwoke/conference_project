# conference/models.py
from django.db import models

class Conference(models.Model):
    name = models.CharField(max_length=255)
    dates = models.DateTimeField()
    location = models.CharField(max_length=255)
    topics = models.CharField(max_length=255)
