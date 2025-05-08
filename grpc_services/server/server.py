import grpc
from concurrent import futures
import random
import transport_pb2
import transport_pb2_grpc
from concurrent import futures


class TransportService(transport_pb2_grpc.TransportServiceServicer):
    
    def GetBestItinerary(self, request, context):
        # Logique pour calculer le meilleur itinéraire
        origin = request.origin
        destination = request.destination
        estimated_time = self.calculate_estimated_time(origin, destination)
        transport_type = self.determine_transport_type()

        return transport_pb2.ItineraryResponse(
            route=f"Route de {origin} à {destination}",
            transport_type=transport_type,
            estimated_time=estimated_time
        )

    def PredictTraffic(self, request, context):
        # Logique pour prédire le trafic
        origin = request.origin
        destination = request.destination
        datetime = request.datetime
        traffic_level = self.simulate_traffic(origin, destination, datetime)

        return transport_pb2.TrafficResponse(level=traffic_level)

    def ListTransportsAvailable(self, request, context):
        # Logique pour lister les types de transports disponibles
        zone = request.zone
        transports = self.get_transports_for_zone(zone)

        return transport_pb2.TransportList(transports=transports)

    def calculate_estimated_time(self, origin, destination):
        # Simule le temps estimé en fonction de l'origine et de la destination
        return random.uniform(10, 60)  # temps estimé entre 10 et 60 minutes

    def determine_transport_type(self):
        # Simule la détermination du type de transport
        transports = ["car", "bus", "tram", "taxi"]
        return random.choice(transports)

    def simulate_traffic(self, origin, destination, datetime):
        # Simule le niveau de trafic en fonction de l'origine, de la destination et de la date/heure
        traffic_levels = ["Low", "Moderate", "High"]
        return random.choice(traffic_levels)

    def get_transports_for_zone(self, zone):
        # Simule la liste des types de transports disponibles dans une zone donnée
        available_transports = ["car", "bus", "tram", "taxi"]
        return available_transports

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    transport_pb2_grpc.add_TransportServiceServicer_to_server(TransportService(), server)
    server.add_insecure_port('[::]:50051')
    print("gRPC server started on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
