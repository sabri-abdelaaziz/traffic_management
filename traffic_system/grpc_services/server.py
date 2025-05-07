import grpc
from concurrent import futures
import time

import grpc_services.transport_pb2 as transport_pb2
import grpc_services.transport_pb2_grpc as transport_pb2_grpc

class TransportServiceServicer(transport_pb2_grpc.TransportServiceServicer):
    def GetBestTransport(self, request, context):
        print(f"Received: {request.start_point} to {request.end_point}")
        # Exemple simple : retourne le bus comme meilleur transport
        return transport_pb2.TransportResponse(
            transport_type="bus",
            estimated_time=15.0
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    transport_pb2_grpc.add_TransportServiceServicer_to_server(TransportServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC Server running on port 50051...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
