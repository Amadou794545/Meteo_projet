import os

import pandas as pd

from src.Interface.IDataCleaner import IDataCleaner


class DataCleaner(IDataCleaner):

    def __init__(self, temperature_range=(-50, 50), station_name="unknown_station"):
        self.temperature_min, self.temperature_max = temperature_range
        self.station_name = station_name

    def clean_data(self, data) -> pd.DataFrame:
        if data is None or data.empty:
            raise ValueError("Le DataFrame fourni est vide ou invalide.")
        # Ajouter la colonne `nom_station`
        data['nom_station'] = self.station_name



        # Appliquer les étapes de nettoyage
        data = self._remove_missing_values(data)
        data = self._filter_outliers(data)
        data = self._remove_doublons(data)

        return data

    # supprimer les ligne identiques dans les colonnes 'heure_de_paris' et 'nom_station'
    def _remove_doublons(self, data):
        return data.drop_duplicates(subset=['heure_de_paris', 'nom_station'])

    def _remove_missing_values(self, data):
        return data.dropna()

    def _filter_outliers(self, data):
        return data[
            (data['temperature_en_degre_c'] >= self.temperature_min) &
            (data['temperature_en_degre_c'] <= self.temperature_max)
            ]
