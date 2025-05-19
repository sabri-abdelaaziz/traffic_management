# flink_service.py
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types
import requests

def call_transport_api(zone):
    try:
        url = f"http://localhost:8000/transports?zone={zone}"
        response = requests.get(url)
        data = response.json()
        return f"Zone: {zone}, Transports disponibles: {data.get('available_transports', [])}"
    except Exception as e:
        return f"Erreur appel API pour zone {zone} : {e}"

def main():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)

    # Exemple de données entrantes
    zones = env.from_collection(
        collection=["Centre", "Nord", "Sud"],
        type_info=Types.STRING()
    )

    # Appeler l’API REST pour chaque zone
    results = zones.map(lambda zone: call_transport_api(zone), output_type=Types.STRING())

    # Affichage des résultats
    results.print()

    env.execute("Flink Transport Recommendation Job")

if __name__ == '__main__':
    main()
