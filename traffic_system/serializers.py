from rest_framework import serializers
from .models import User, Transport, Itinerary, TrafficData

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# Même chose pour les autres modèles
