"""CSV-based storage implementation for weather records."""

import os

import pandas as pd

from src.Interface.IDataStorage import IDataStorage
from src.collectors.APIDataCollector import APIDataCollector


class CSVStorage(IDataStorage):
    """Persist and refresh weather data using a CSV file."""

    def __init__(self, file_path: str, collector: APIDataCollector):
        self.file_path = file_path
        self.collector = collector

    def save_data(self, data: pd.DataFrame) -> None:
        """Append data to CSV, adding headers when the file is created."""
        file_exists = os.path.isfile(self.file_path)
        data.to_csv(self.file_path, mode="a", header=not file_exists, index=False)
        print(f"✅ Données sauvegardées dans : {self.file_path}")

    def load_data(self, key: str) -> pd.DataFrame:  # pylint: disable=unused-argument
        """Reload the latest data directly from the API collector."""
        print("🔄 Rechargement des données depuis l'API...")
        data = self.collector.collect_data()
        print("✅ Données mises à jour récupérées depuis l'API.")
        return data

    def delete_data(self, key: str) -> None:  # pylint: disable=unused-argument
        """Clear the CSV file content."""
        with open(self.file_path, "w", encoding="utf-8"):
            pass
        print(f"✅ Données supprimées dans : {self.file_path}")
