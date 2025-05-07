# import grpc
# from grpc_services import transport_pb2, transport_pb2_grpc

# def get_best_itinerary(origin, destination):
#     channel = grpc.insecure_channel('localhost:50051')
#     stub = transport_pb2_grpc.TransportServiceStub(channel)
#     response = stub.GetBestItinerary(transport_pb2.ItineraryRequest(origin=origin, destination=destination))
#     return {
#         "route": response.route,
#         "transport_type": response.transport_type,
#         "estimated_time": response.estimated_time
#     }

# def predict_traffic(origin, destination, datetime):
#     channel = grpc.insecure_channel('localhost:50051')
#     stub = transport_pb2_grpc.TransportServiceStub(channel)
#     response = stub.PredictTraffic(transport_pb2.TrafficRequest(origin=origin, destination=destination, datetime=datetime))
#     return {"level": response.level}

# def list_transports(zone):
#     channel = grpc.insecure_channel('localhost:50051')
#     stub = transport_pb2_grpc.TransportServiceStub(channel)
#     response = stub.ListTransportsAvailable(transport_pb2.TransportRequest(zone=zone))
#     return {"transports": list(response.transports)}
