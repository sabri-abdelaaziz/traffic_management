from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()

class Transport(models.Model):
    type = models.CharField(max_length=50)  # bus, tramway, etc.
    speed = models.FloatField()
    capacity = models.IntegerField()

class Itinerary(models.Model):
    start_point = models.CharField(max_length=255)
    end_point = models.CharField(max_length=255)
    estimated_time = models.FloatField()

class TrafficData(models.Model):
    location = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    congestion_level = models.IntegerField()  # e.g., 1 to 5
