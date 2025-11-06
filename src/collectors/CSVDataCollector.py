import pandas as pd

from src.Interface.IDataCollector import IDataCollector


class CSVDataCollector(IDataCollector):
    def __init__(self, file_path):
        self.file_path = file_path

    def collect_data(self):
        print(f"📥 Collecte des données depuis : {self.file_path}")
        return pd.read_csv(self.file_path)