from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.city} ({self.code})"
    
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")    # cascade means if airport is deleted, all flights from that airport will be deleted
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")     
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
    
class Passenger(models.Model):
    first = models.CharField(max_length=60)
    last = models.CharField(max_length=60)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")    # blank=True means that the field is not required

    def __str__(self):
        return f"{self.first} {self.last}"