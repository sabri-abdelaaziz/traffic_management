# transport_api/simulation.py

import random

nodes = {
    "Hay Riad": (34.01, -6.85),
    "Agdal": (34.00, -6.83),
    "Centre Ville": (34.02, -6.84),
}

edges = [
    {"from": "Hay Riad", "to": "Agdal", "distance": 3.0, "transport": ["Bus", "Taxi"]},
    {"from": "Agdal", "to": "Centre Ville", "distance": 2.0, "transport": ["Taxi"]},
    {"from": "Hay Riad", "to": "Centre Ville", "distance": 4.5, "transport": ["Tramway"]},
]

def simulate_traffic_level():
    return random.choice(["Low", "Moderate", "High"])
