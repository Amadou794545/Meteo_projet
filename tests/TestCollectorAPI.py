from src.collectors.APIDataCollector import APIDataCollector


class APIClient:
    base_url = ("https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/13-station-meteo-toulouse-pech"
                "-david/records?select=id%2Ctype_de_station%2Ctemperature_en_degre_c%2C%20pluie%2Chumidite%2Cpression"
                "%2Cheure_de_paris")
    params = {"limit": 100}


client = APIClient()
collector = APIDataCollector(client)

df = collector.collect_data()
print(df)
