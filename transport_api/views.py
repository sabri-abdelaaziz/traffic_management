from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .grpc_client import get_best_itinerary, predict_traffic, list_transports
from django.http import JsonResponse
import random
from datetime import datetime

import random
from django.http import JsonResponse


def simulate_traffic_per_zone(request):
    zones = {
    "Stade Mohammed V": [33.5888, -7.6306],
    "Gare Casa-Voyageurs": [33.6034, -7.6142],
    "Gare Casa-Port": [33.6056, -7.6131],
    "Maarif": [33.5883, -7.6246],
    "Ain Sebaa": [33.6167, -7.5167],
    "Hay Hassani": [33.5667, -7.6667],
    "Derb Ghallef": [33.5800, -7.6250],
    "Oasis": [33.5668, -7.6306],
    "Sidi Maarouf": [33.5390, -7.6293],
    "Quartier des Hôpitaux": [33.5770, -7.6186],
    "Bourgogne": [33.5951, -7.6460],
    "Anfa": [33.5892, -7.6593],
    "Palmier": [33.5791, -7.6248],
    "Mers Sultan": [33.5808, -7.6003],
    "Roches Noires": [33.6040, -7.5810],
    "Hay Mohammadi": [33.6045, -7.5584],
    "La Gironde": [33.5833, -7.6056],
    "Les Hôpitaux": [33.5725, -7.6180],
    "Bd Zerktouni": [33.5885, -7.6185],
    "Gauthier": [33.5895, -7.6328],
    "Corniche Aïn Diab": [33.5800, -7.6840],
    "Morocco Mall": [33.5595, -7.6911],
    "Technopark": [33.5552, -7.6523],
    "Casa Nearshore": [33.5235, -7.6420],
    "Hay Lalla Meriem": [33.5511, -7.6233],
    "Hay Nahda": [33.5633, -7.5733],
    "Hay El Fida": [33.5867, -7.5870],
    "Derb Sultan": [33.5720, -7.5933],
    "Aïn Chock": [33.5450, -7.6020],
    "Sbata": [33.5620, -7.5670],
    "Hay Errahma": [33.5010, -7.6550],
    "Tachfine Center": [33.5835, -7.5837],
    "Bab Marrakech (ancienne médina)": [33.6012, -7.6125],
    "Bd Moulay Slimane": [33.6073, -7.5995],
    "Twin Center": [33.5829, -7.6336],
    "Université Hassan II": [33.5482, -7.6551],
}


    levels = ["Low", "Moderate", "High"]
    traffic = []

    for name, coords in zones.items():
        traffic.append({
            "zone": name,
            "lat": coords[0],
            "lon": coords[1],
            "level": random.choice(levels)
        })

    return JsonResponse({"traffic": traffic})
def simulation_page(request):
    return render(request, "simulation.html")

def simulate_traffic_api(request):
    level = random.choice(["Faible", "Modéré", "Fort"])
    return JsonResponse({"level": level})
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
def weighted_traffic():
    hour = datetime.now().hour
    if 7 <= hour <= 9 or 17 <= hour <= 19:
        return random.choices(["High", "Moderate", "Low"], weights=[5, 3, 2])[0]
    else:
        return random.choices(["Low", "Moderate", "High"], weights=[5, 3, 2])[0]
    