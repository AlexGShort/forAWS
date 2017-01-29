from __future__ import unicode_literals

from django.db import models
from ..login.models import User

# Create your models here.
class Trip(models.Model):
    destination = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    date_from = models.DateField()
    date_to = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    participant = models.ManyToManyField(User, related_name='participantToTrip')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
