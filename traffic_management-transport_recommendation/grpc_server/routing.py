import networkx as nx
import osmnx as ox
import os

try:
    graph_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'city_map.graphml')
    graph_path = os.path.abspath(graph_path)
    G = ox.load_graphml(graph_path)
except Exception as e:
    print(f"Erreur lors du chargement du graphe : {e}")
    G = None

def calculate_route(start_coords, end_coords):
    if G is None:
        return [], 0

    try:
        orig_node = ox.distance.nearest_nodes(G, X=start_coords[1], Y=start_coords[0])
        dest_node = ox.distance.nearest_nodes(G, X=end_coords[1], Y=end_coords[0])

        route = nx.shortest_path(G, orig_node, dest_node, weight='length')

        path_coords = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in route]

        # Calculer la distance totale du chemin en mètres (somme des poids 'length' des arêtes)
        distance = 0
        for i in range(len(route) - 1):
            edge_data = G.get_edge_data(route[i], route[i+1])
            # edge_data peut être un dict avec plusieurs clés (multi-graph), on prend la première arête
            if edge_data:
                if isinstance(edge_data, dict):
                    edge = list(edge_data.values())[0]
                else:
                    edge = edge_data
                distance += edge.get('length', 0)

        return [f"{lat},{lng}" for lat, lng in path_coords], distance / 1000  # Converti en km

    except Exception as e:
        print(f"Erreur lors du calcul de l'itinéraire : {e}")
        return [], 0
