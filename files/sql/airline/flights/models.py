from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField

# Create your models here.

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.code} ({self.city})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField() 

    def __str__(self):
        return f"{self.id}:{self.origin} to {self.destination}"