import pandas as pd
from src.Interface.IDataStorage import IDataStorage
import csv


class CSVStorage(IDataStorage):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def save(self, data: pd.DataFrame):
        with open(self.file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            for row in data:
                writer.writerow(row)
        print(f" Données sauvegardées dans : {self.file_path}")

    def load(self):
        data = []
        with open(self.file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        return data
        print(f" Données chargées depuis : {self.file_path}")

    def delete(self):
        open(self.file_path, 'w').close()
        print(f" Données supprimées dans : {self.file_path}")
