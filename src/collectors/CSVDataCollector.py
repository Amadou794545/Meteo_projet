"""Collector implementation that reads weather records from a CSV file."""

import pandas as pd

from src.Interface.IDataCollector import IDataCollector


class CSVDataCollector(IDataCollector):  # pylint: disable=too-few-public-methods
    """Load weather data from a local CSV source."""

    def __init__(self, file_path):
        self.file_path = file_path

    def collect_data(self):
        """Read and return CSV rows as a pandas DataFrame."""
        print(f"📥 Collecte des données depuis : {self.file_path}")
        return pd.read_csv(self.file_path)
