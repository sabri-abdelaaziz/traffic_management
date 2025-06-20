def recommend_transport(path):
    if not path:
        return "Aucun trajet disponible"
    length = len(path)
    if length <= 5:
        return "Taxi"
    elif length <= 20:
        return "Tramway"
    else:
        return "Bus"
