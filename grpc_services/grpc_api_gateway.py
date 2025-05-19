# grpc_api_gateway.py
from fastapi import FastAPI
from pydantic import BaseModel
import grpc
from . import itinerary_pb2, itinerary_pb2_grpc
import traffic_pb2
import traffic_pb2_grpc
import transport_pb2
import transport_pb2_grpc

# Déclaration de l'application FastAPI
app = FastAPI()

# Connexion au serveur gRPC (ajuste le port si besoin)
channel = grpc.insecure_channel('localhost:50051')
itinerary_stub = itinerary_pb2_grpc.ItineraryServiceStub(channel)
traffic_stub = traffic_pb2_grpc.TrafficPredictionServiceStub(channel)
transport_stub = transport_pb2_grpc.TransportServiceStub(channel)

# Modèles pour les requêtes POST si besoin
class ItineraryRequest(BaseModel):
    origin: str
    destination: str

class TrafficRequest(BaseModel):
    origin: str
    destination: str
    datetime: str

class TransportRequest(BaseModel):
    zone: str

@app.get("/")
def root():
    return {"message": "GRPC Gateway API is running."}

@app.get("/itinerary")
def get_itinerary(origin: str, destination: str):
    request = itinerary_pb2.ItineraryRequest(origin=origin, destination=destination)
    response = itinerary_stub.GetBestItinerary(request)
    return {"transport": response.transport, "duration": response.duration}

@app.get("/traffic")
def predict_traffic(origin: str, destination: str, datetime: str):
    request = traffic_pb2.TrafficRequest(origin=origin, destination=destination, datetime=datetime)
    response = traffic_stub.PredictTraffic(request)
    return {"traffic_level": response.traffic_level}

@app.get("/transports")
def list_transports(zone: str):
    request = transport_pb2.TransportRequest(zone=zone)
    response = transport_stub.ListAvailableTransports(request)
    return {"available_transports": list(response.available_transports)}
