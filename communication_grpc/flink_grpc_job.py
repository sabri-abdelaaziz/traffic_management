import grpc
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common import Types

import transport_pb2
import transport_pb2_grpc


def call_grpc(origin, destination):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = transport_pb2_grpc.TransportServiceStub(channel)
        request = transport_pb2.ItineraryRequest(origin=origin, destination=destination)
        response = stub.GetBestItinerary(request)
        return f"{response.route} | {response.transport_type} | {response.estimated_time} min"


def main():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)

    data = env.from_collection(
        collection=[("Casablanca", "Rabat"), ("Rabat", "Fès")],
        type_info=Types.TUPLE([Types.STRING(), Types.STRING()])
    )

    result = data.map(
        lambda x: call_grpc(x[0], x[1]),
        output_type=Types.STRING()
    )

    result.print()

    env.execute("Flink gRPC Communication Job")


if __name__ == '__main__':
    main()
