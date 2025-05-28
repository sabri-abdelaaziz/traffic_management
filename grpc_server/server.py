import grpc
from concurrent import futures
import time
import random
import sys
import os

# Add proto folder to sys.path to import generated modules
proto_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'proto')
sys.path.insert(0, proto_dir)

from concurrent import futures
import grpc
import time

import transport_pb2
import transport_pb2_grpc

class TransportService(transport_pb2_grpc.TransportServiceServicer):
    def GetRoute(self, request, context):
        # Your existing logic
        return transport_pb2.RouteResponse(
            path=["34.056,-118.236", "35.000,-119.000"],
            transport_mode="car",
            distance=45.6
        )

    def StreamVehicles(self, request, context):
        # Simulate streaming vehicle positions
        vehicles = [
            ("vehicle_1", 34.056, -118.236),
            ("vehicle_2", 35.000, -119.000)
        ]
        for v in vehicles:
            yield transport_pb2.VehiclePosition(vehicle_id=v[0], lat=v[1], lng=v[2])
            time.sleep(1)
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    transport_pb2_grpc.add_TransportServiceServicer_to_server(TransportService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC Server running on port 50051")
    server.wait_for_termination()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
