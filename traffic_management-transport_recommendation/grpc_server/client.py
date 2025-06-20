import grpc
import transport_pb2
import transport_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = transport_pb2_grpc.TransportServiceStub(channel)

    # Exemple : Casablanca centre à un autre point
    request = transport_pb2.RouteRequest(
        start_lat=33.5731,
        start_lng=-7.5898,
        end_lat=33.5975,
        end_lng=-7.6192
    )

    response = stub.GetRoute(request)
    print("Chemin calculé:")
    for point in response.path:
        print(point)
    print("Moyen de transport recommandé:", response.transport_mode)

if __name__ == "__main__":
    run()
