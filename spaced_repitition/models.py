from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Deck(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class Card(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    decks = models.ManyToManyField(Deck)
    days_till_study = models.IntegerField(default=1)

    def __str__(self):
        return self.question + ' pk: ' + str(self.pk)
