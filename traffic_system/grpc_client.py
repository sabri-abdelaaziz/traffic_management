import grpc
from grpc_services import transport_pb2, transport_pb2_grpc

def get_best_transport(start_point, end_point):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = transport_pb2_grpc.TransportServiceStub(channel)
        request = transport_pb2.TransportRequest(start_point=start_point, end_point=end_point)
        response = stub.GetBestTransport(request)
        return response.transport_type, response.estimated_time
