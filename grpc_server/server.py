import random
import grpc
from concurrent import futures
import time
import sys
import os

# Add proto folder to sys.path to import generated modules
proto_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'proto')
sys.path.insert(0, proto_dir)

import transport_pb2
import transport_pb2_grpc
from routing import calculate_route
from recommender import recommend_transport

# Dummy vehicle data
vehicles = [
    {"id": "vehicle_1", "lat": 34.056, "lng": -118.236},
    {"id": "vehicle_2", "lat": 35.000, "lng": -119.000},
]

class TransportServiceServicer(transport_pb2_grpc.TransportServiceServicer):
    def GetRoute(self, request, context):
        start = (request.start_lat, request.start_lng)
        end = (request.end_lat, request.end_lng)

        path, distance = calculate_route(start, end)
        transport_mode = recommend_transport(path)

        return transport_pb2.RouteResponse(
            path=path,
            transport_mode=transport_mode,
            distance=distance
        )

    def StreamVehicles(self, request, context):
        # Infinite streaming of vehicle positions with simulated movement
        while True:
            for v in vehicles:
                # Optionally simulate some movement
                v["lat"] += (0.001 * (0.5 - random.random()))
                v["lng"] += (0.001 * (0.5 - random.random()))

                yield transport_pb2.Vehicle(
                    id=v["id"],
                    lat=v["lat"],
                    lng=v["lng"]
                )
                time.sleep(1)  # simulate delay

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    transport_pb2_grpc.add_TransportServiceServicer_to_server(TransportServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("gRPC server running on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
