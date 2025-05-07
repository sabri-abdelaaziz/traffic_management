from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .grpc_client import get_best_transport

# Create your views here.
from rest_framework import viewsets
from .models import User, Transport, Itinerary, TrafficData
from .serializers import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Même logique pour les autres entités
@api_view(['GET'])
def get_best_transport(request):
    # logique simple d'exemple
    itinerary_id = request.GET.get('id')
    itinerary = Itinerary.objects.get(id=itinerary_id)
    transports = Transport.objects.all()

    # calculer le "meilleur" (ex: celui avec le temps le plus bas)
    best = min(transports, key=lambda t: itinerary.estimated_time / t.speed)
    serializer = TransportSerializer(best)
    return Response(serializer.data)

def predict_congestion(location):
    now = timezone.now()
    past_data = TrafficData.objects.filter(location=location, timestamp__hour=now.hour)
    avg_level = sum(d.congestion_level for d in past_data) / len(past_data)
    return avg_level



@api_view(['GET'])
def recommended_transport(request):
    start = request.GET.get('start', 'Point A')
    end = request.GET.get('end', 'Point B')
    transport, time = get_best_transport(start, end)
    return Response({
        "recommended_transport": transport,
        "estimated_time": time
    })