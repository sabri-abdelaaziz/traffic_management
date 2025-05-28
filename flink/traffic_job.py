from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types
import grpc
from google.protobuf import empty_pb2
import sys
import os

# Adjust sys.path to import generated gRPC code
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'grpc_server')))

import transport_pb2
import transport_pb2_grpc


def fetch_vehicle_positions(limit=10):
    channel = grpc.insecure_channel('localhost:50051')
    stub = transport_pb2_grpc.TransportServiceStub(channel)

    results = []
    try:
        for i, vehicle in enumerate(stub.StreamVehicles(empty_pb2.Empty())):
            # Correct field name: 'id'
            print(f"Receiving from gRPC: {vehicle.id}, {vehicle.lat}, {vehicle.lng}")
            results.append((vehicle.id, vehicle.lat, vehicle.lng))
            if i >= limit - 1:
                break
    except grpc.RpcError as e:
        print(f"gRPC error: {e}")
    return results


def main():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)

    vehicle_data = fetch_vehicle_positions(limit=5)

    data_stream = env.from_collection(
        collection=vehicle_data,
        type_info=Types.TUPLE([Types.STRING(), Types.DOUBLE(), Types.DOUBLE()])
    )

    data_stream \
        .map(lambda x: f"Vehicle {x[0]} at position ({x[1]:.5f}, {x[2]:.5f})") \
        .print()

    env.execute("gRPC Vehicle Streaming Job")


if __name__ == "__main__":
    main()
