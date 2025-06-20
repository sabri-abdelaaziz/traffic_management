import osmnx as ox

def generate_casablanca_graph():
    print("Téléchargement du réseau routier de Casablanca depuis OpenStreetMap...")
    G = ox.graph_from_place("Casablanca, Morocco", network_type="drive")
    
    print("Sauvegarde dans data/city_map.graphml ...")
    ox.save_graphml(G, filepath="data/city_map.graphml")
    print("Fichier city_map.graphml créé avec succès !")

if __name__ == "__main__":
    generate_casablanca_graph()
