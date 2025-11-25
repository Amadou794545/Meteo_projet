import os

import pandas as pd
from src.Interface.IDataStorage import IDataStorage
from src.collectors.APIDataCollector import APIDataCollector


class CSVStorage(IDataStorage):
    def __init__(self, file_path: str, collector: APIDataCollector):

        self.file_path = file_path
        self.collector = collector

    def save_data(self, data: pd.DataFrame) -> None:

        file_exists = os.path.isfile(self.file_path)

        # Ajoute les données au fichier existant ou crée un nouveau fichier
        data.to_csv(self.file_path, mode='a', header=not file_exists, index=False)
        print(f"✅ Données sauvegardées dans : {self.file_path}")

    def load_data(self, key: str) -> pd.DataFrame:

        print("🔄 Rechargement des données depuis l'API...")
        data = self.collector.collect_data()
        print("✅ Données mises à jour récupérées depuis l'API.")
        return data

    def delete_data(self, key: str) -> None:

        open(self.file_path, 'w').close()
        print(f"✅ Données supprimées dans : {self.file_path}")