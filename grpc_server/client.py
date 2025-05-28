from flask import Flask, render_template, request, jsonify
import grpc
import os
import sys

# Add grpc_server folder to sys.path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'grpc_server')))

from transport_pb2 import RouteRequest
from transport_pb2_grpc import TransportServiceStub

app = Flask(__name__)

def grpc_get_route(start_lat, start_lng, end_lat, end_lng):
    channel = grpc.insecure_channel('localhost:50051')
    stub = TransportServiceStub(channel)
    request = RouteRequest(
        start_lat=start_lat,
        start_lng=start_lng,
        end_lat=end_lat,
        end_lng=end_lng
    )
    response = stub.GetRoute(request)
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_route', methods=['POST'])
def calculate_route():
    data = request.get_json()
    start_lat = data['start_lat']
    start_lng = data['start_lng']
    end_lat = data['end_lat']
    end_lng = data['end_lng']

    response = grpc_get_route(start_lat, start_lng, end_lat, end_lng)

    path_coords = []
    for point_str in response.path:
        lat_str, lng_str = point_str.split(',')
        path_coords.append([float(lat_str), float(lng_str)])

    distance = getattr(response, 'distance', None)

    return jsonify({
        'path': path_coords,
        'transport_mode': response.transport_mode,
        'distance': distance
    })

if __name__ == '__main__':
    app.run(debug=True)
