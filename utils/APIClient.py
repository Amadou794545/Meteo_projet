class APIClient:
    def __init__(self, base_url, limit=100):
        self.base_url = base_url
        self.params = {
            "limit": limit,
            "select": "id,type_de_station,temperature_en_degre_c,pluie,humidite,pression,heure_de_paris",
            "order_by": "heure_de_paris DESC"
        }


STATIONS = {
        "montaudran": "https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/12-station-meteo-toulouse-montaudran/records",
        "pech-david": "https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/13-station-meteo-toulouse-pech-david/records",
        "compans-cafarelli": "https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/42-station-meteo-toulouse-parc-compans-cafarelli/records",
        "marengo": "https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/02-station-meteo-toulouse-marengo/records"
    }