from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Card(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
