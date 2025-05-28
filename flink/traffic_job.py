from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types
from google.protobuf import empty_pb2
import grpc
import time

# Adjust path to import transport_pb2 and transport_pb2_grpc
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'grpc_server')))

import transport_pb2
import transport_pb2_grpc


def fetch_vehicle_positions(limit=10):
    """Connects to gRPC server and yields a limited number of vehicle positions."""
    channel = grpc.insecure_channel('localhost:50051')
    stub = transport_pb2_grpc.TransportServiceStub(channel)

    results = []
    try:
        for i, vehicle in enumerate(stub.StreamVehicles(empty_pb2.Empty())):
            print(f"Receiving from gRPC: {vehicle.vehicle_id}, {vehicle.lat}, {vehicle.lng}")
            results.append((vehicle.vehicle_id, vehicle.lat, vehicle.lng))
            if i >= limit - 1:
                break
    except grpc.RpcError as e:
        print(f"gRPC error: {e}")
    return results


def main():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)

    # Fetch a batch of live vehicle positions from gRPC
    vehicle_data = fetch_vehicle_positions(limit=5)

    # Feed to Flink as a batch source (simulating stream)
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
