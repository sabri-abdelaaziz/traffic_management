from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .grpc_client import get_best_itinerary, predict_traffic, list_transports

def index(request):
    return render(request, 'index.html')


@api_view(['GET'])
def best_itinerary_view(request):
    origin = request.GET.get('origin')
    destination = request.GET.get('destination')
    data = get_best_itinerary(origin, destination)
    return Response(data)

@api_view(['GET'])
def predict_traffic_view(request):
    origin = request.GET.get('origin')
    destination = request.GET.get('destination')
    datetime = request.GET.get('datetime')
    data = predict_traffic(origin, destination, datetime)
    return Response(data)

@api_view(['GET'])
def list_transports_view(request):
    zone = request.GET.get('zone')
    data = list_transports(zone)
    return Response(data)
