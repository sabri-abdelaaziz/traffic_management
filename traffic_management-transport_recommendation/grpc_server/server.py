from concurrent import futures
import grpc
import transport_pb2
import transport_pb2_grpc
from routing import calculate_route
from recommender import recommend_transport

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

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    transport_pb2_grpc.add_TransportServiceServicer_to_server(TransportServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("Serveur gRPC en cours d'exécution sur le port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
