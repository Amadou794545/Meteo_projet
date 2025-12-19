class APIClient:
    _instance = None

    def __new__(cls, base_url, limit=100):
        if cls._instance is None:
            cls._instance = super(APIClient, cls).__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self, base_url, limit=100):
        if not self.__initialized:
            self.base_url = base_url
            self.params = {
                "limit": limit,
                "select": "id,type_de_station,temperature_en_degre_c,pluie,humidite,pression,heure_de_paris",
                "order_by": "heure_de_paris DESC"
            }
            self.__initialized = True


STATIONS = {
        "montaudran": "https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/12-station-meteo-toulouse-montaudran/records",
        "pech-david": "https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/13-station-meteo-toulouse-pech-david/records",
        "compans-cafarelli": "https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/42-station-meteo-toulouse-parc-compans-cafarelli/records",
        "marengo": "https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/02-station-meteo-toulouse-marengo/records"
    }