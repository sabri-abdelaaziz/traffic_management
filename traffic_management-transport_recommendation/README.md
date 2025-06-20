# Transport Recommendation System

A web application that provides transport recommendations and cost estimations for routes in Morocco.

## Features

- Interactive map interface with OpenStreetMap integration
- Location search with autocomplete
- Route calculation and visualization
- Transport mode recommendations based on distance
- Cost estimation for different transport options
- User feedback system with ratings and comments
- Modern, responsive UI with dark theme

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd transport_recommendation
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Start the gRPC server:
```bash
python grpc_server/server.py
```

5. Start the frontend server:
```bash
python frontend/app.py
```

The application will be available at http://localhost:5000

## Project Structure

```
transport_recommendation/
├── frontend/            # Frontend Flask application
├── grpc_server/        # gRPC server implementation
├── grpc_client/        # gRPC client code
├── proto/              # Protocol buffer definitions
├── data/              # Data files and resources
└── cache/             # Cache directory
```

## Technologies Used

- Flask for web server
- gRPC for microservices communication
- OpenStreetMap for maps and geocoding
- Modern CSS with Flexbox and Grid
- Font Awesome icons

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 