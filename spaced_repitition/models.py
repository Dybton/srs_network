from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Deck(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Card(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    # Tror måske, at jeg skal gøre denne til en one to many? Og så genere et nyt id til hvert kort der bliver ændret - eller hvad? Men hvad nu hvis personen redigerer i kortet?
    decks = models.ManyToManyField(Deck)
    days_till_study = models.IntegerField(default=1)

    def __str__(self):
        return self.question
