from src.cleaners.DataCleaner import DataCleaner
from src.collectors.APIDataCollector import APIDataCollector
from src.storage.CSVStorage import CSVStorage


class DataPipeline:
    def __init__(self, collector: APIDataCollector, cleaner: DataCleaner, storage: CSVStorage, visualizer):
        self.collector = collector
        self.cleaner = cleaner
        self.storage = storage
        self.visualizer = visualizer

    def run(self, output_path):
        # Étape 1 : Collecte
        data = self.collector.collect_data()  # Exemple de mappage des données récupérées

        # Étape 2 : Nettoyage
        data = self.cleaner.clean_data(data)

        # Étape 3 : Sauvegarde
        self.storage.save_data(data=data)

        # Étape 4 : Visualisation
        # à faire
        self.visualizer.visualize(data)

        # faire les prédiction
        #
        # renvoie la première ligne du dataframe pour vérification
        return data.head(1)

        print("✅ Pipeline exécuté avec succès.")
