from concurrent import futures
import grpc
import transport_pb2 as pb2
import transport_pb2_grpc as pb2_grpc
from geopy.distance import geodesic

import datetime

transport_options = [
    {"type": "Bus", "speed_kmh": 30, "cost_per_km": 0.5},
    {"type": "Train", "speed_kmh": 80, "cost_per_km": 1.0},
    {"type": "Taxi", "speed_kmh": 50, "cost_per_km": 3.0},
]

def compute_best_itinerary(origin, destination):
    # coordonnées fictives pour test
    locations = {
        "Casablanca": (33.5731, -7.5898),
        "Rabat": (34.020882, -6.841650),
        "Fès": (34.0331, -5.0003),
    }

    coord1 = locations.get(origin)
    coord2 = locations.get(destination)

    if not coord1 or not coord2:
        return None

    distance_km = geodesic(coord1, coord2).km

    best = None
    for opt in transport_options:
        time_h = distance_km / opt["speed_kmh"]
        cost = distance_km * opt["cost_per_km"]
        if not best or time_h < best["estimated_time"]:
            best = {
                "route": f"{origin} -> {destination}",
                "transport_type": opt["type"],
                "estimated_time": round(time_h * 60, 2),  # minutes
            }
    return best


def predict_traffic_level(origin, destination, datetime_str):
    hour = int(datetime_str.split("T")[1].split(":")[0])
    if 7 <= hour <= 9 or 17 <= hour <= 19:
        return "Fort"
    elif 10 <= hour <= 16:
        return "Modéré"
    else:
        return "Fluide"

zone_transports = {
    "Casablanca": ["Tramway", "Bus", "Taxi"],
    "Rabat": ["Bus", "Taxi"],
    "Fès": ["Taxi"],
}

def get_transports_for_zone(zone):
    return zone_transports.get(zone, [])

class TransportService(pb2_grpc.TransportServiceServicer):
    def GetBestItinerary(self, request, context):
        return pb2.ItineraryResponse(
            route=f"{request.origin} -> {request.destination} via Autoroute",
            transport_type="Train",
            estimated_time=90.0
        )

    def PredictTraffic(self, request, context):
        return pb2.TrafficResponse(level="Modéré")

    def ListTransportsAvailable(self, request, context):
        return pb2.TransportList(transports=["Bus", "Taxi", "Tramway"])

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    pb2_grpc.add_TransportServiceServicer_to_server(TransportService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server running on port 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
