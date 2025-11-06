from DataPipeline import DataPipeline
from src.collectors.APIDataCollector import APIDataCollector


class APIClient:
    base_url = "https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/13-station-meteo-toulouse-pech-david/records"
    params = {
        "limit": 100,
        "select": "id,type_de_station,temperature_en_degre_c,pluie,humidite,pression,heure_de_paris"
    }


client = APIClient()
collector = APIDataCollector(client)


pipeline = DataPipeline(
    collector=collector,
    cleaner=None,
    storage=None,
    visualizer=None
)

pipeline.run(output_path="output.csv")
