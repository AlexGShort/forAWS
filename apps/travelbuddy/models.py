from __future__ import unicode_literals

from django.db import models
from ..models import User

# Create your models here.
class Trip(models.Models):
    destination = CharField(max_length=100)
    description = TextField(max_length=1000)
    date_from = DateTimeField()
    date_to = DateTimeField()
    owner = ForeignKey(User, on_delete=models.CASCADE)
    participant = ManyToManyField(User)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
