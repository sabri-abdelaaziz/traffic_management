import grpc
from concurrent import futures
import grpc_services.proto.transport_pb2_grpc as transport_pb2_grpc
import grpc_services.proto.transport_pb2 as transport_pb2
from transport_api.models import TrafficEvent
from datetime import datetime

class TrafficDataServicer(transport_pb2_grpc.TrafficDataServicer):
    def SendEvent(self, request, context):
        TrafficEvent.objects.create(
            agent_type=request.agent_type,
            from_zone=request.from_zone,
            to_zone=request.to_zone
        )
        return transport_pb2.Empty()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    transport_pb2_grpc.add_TrafficDataServicer_to_server(TrafficDataServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


