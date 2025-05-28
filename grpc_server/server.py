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

class TransportServiceServicer(transport_pb2_grpc.TransportServiceServicer):
    def GetRoute(self, request, context):
        # Dummy route with straight line and simple data
        path = [
            f"{request.start_lat},{request.start_lng}",
            f"{(request.start_lat + request.end_lat)/2},{(request.start_lng + request.end_lng)/2}",
            f"{request.end_lat},{request.end_lng}"
        ]
        transport_mode = "car"
        distance = 10.5  # dummy km

        return transport_pb2.RouteResponse(path=path, transport_mode=transport_mode, distance=distance)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    transport_pb2_grpc.add_TransportServiceServicer_to_server(TransportServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC Server running on port 50051")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
