from datetime import datetime


class MesureMeteo:
    def __init__(self, temperature: float, humidite: float, pression: float , pluie: float, dataHeure: datetime):
        self.temperature = temperature
        self.humidite = humidite
        self.pression = pression
        self.dataHeure = dataHeure
        self.pluie = pluie

