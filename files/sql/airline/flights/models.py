from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.code} ({self.city})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="derpatures") #"derpatures" será o nome de 'origin' em Airport; 
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField() 

    def __str__(self):
        return f"{self.id}:{self.origin} to {self.destination}"



hnd=Airport(code="HND",city="Tokyo")
gru=Airport(code="GRU",city="Guarulhos")
jfk=Airport(code="JFK",city="New York")
gig=Airport(code="GIG",city="Rio de Janeiro")

f1=Flight(origin= hnd, destination= gru, duration=1400)
f2=Flight(origin= gig, destination= jfk, duration=250)