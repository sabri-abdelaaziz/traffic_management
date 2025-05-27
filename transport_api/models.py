from django.db import models

# Create your models here.

class TrafficEvent(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    agent_type = models.CharField(max_length=20)  # bus, taxi, etc.
    from_zone = models.CharField(max_length=100)
    to_zone = models.CharField(max_length=100)
