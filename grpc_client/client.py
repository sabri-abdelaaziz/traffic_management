import grpc
import sys
import os
import time
import sys
import os

# Add the grpc_server directory to the Python module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../grpc_server')))

import traffic_pb2
import traffic_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = traffic_pb2_grpc.TrafficSimulationStub(channel)

    request = traffic_pb2.StreamRequest(num_agents=3)

    try:
        for response in stub.StreamPositions(request):
            print(f"Agent: {response.agent_id} ({response.agent_type}) at ({response.latitude}, {response.longitude}) status={response.status} time={response.timestamp}")
    except grpc.RpcError as e:
        print(f"RPC failed: {e}")

if __name__ == "__main__":
    run()
