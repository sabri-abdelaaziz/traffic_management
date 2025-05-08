import grpc
#from server import transport_pb2
from grpc_services.server import transport_pb2

#from server import transport_pb2_grpc
from grpc_services.server import transport_pb2_grpc
from django.http import JsonResponse

def get_best_itinerary(origin, destination):
    channel = grpc.insecure_channel('localhost:50051')
    stub = transport_pb2_grpc.TransportServiceStub(channel)

    request = transport_pb2.ItineraryRequest(
        origin=origin,
        destination=destination
    )

    response = stub.GetBestItinerary(request)
    return response.route, response.transport_type, response.estimated_time

# Exemple d'utilisation dans une vue Django

def best_itinerary_view(request):
    origin = request.GET.get('origin')
    destination = request.GET.get('destination')

    route, transport_type, estimated_time = get_best_itinerary(origin, destination)

    return JsonResponse({
        'route': route,
        'transport_type': transport_type,
        'estimated_time': estimated_time
    })
def get_best_itinerary(origin, destination):
    channel = grpc.insecure_channel('localhost:50051')
    stub = transport_pb2_grpc.TransportServiceStub(channel)
    response = stub.GetBestItinerary(transport_pb2.ItineraryRequest(origin=origin, destination=destination))
    return {
        "route": response.route,
        "transport_type": response.transport_type,
        "estimated_time": response.estimated_time
    }

def predict_traffic(origin, destination, datetime):
    channel = grpc.insecure_channel('localhost:50051')
    stub = transport_pb2_grpc.TransportServiceStub(channel)
    response = stub.PredictTraffic(transport_pb2.TrafficRequest(origin=origin, destination=destination, datetime=datetime))
    return {"level": response.level}

def list_transports(zone):
    channel = grpc.insecure_channel('localhost:50051')
    stub = transport_pb2_grpc.TransportServiceStub(channel)
    response = stub.ListTransportsAvailable(transport_pb2.TransportRequest(zone=zone))
    return {"transports": list(response.transports)}