from src.cleaners.DataCleaner import DataCleaner
from src.collectors.APIDataCollector import APIDataCollector
from src.storage.CSVStorage import CSVStorage


class DataPipeline:
    def __init__(self, collector: APIDataCollector, cleaner: DataCleaner, storage: CSVStorage, visualizer):
        self.collector = collector
        self.cleaner = cleaner
        self.storage = storage
        self.visualizer = visualizer

    def run(self):
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


class DataPipelineBuilder:
    def __init__(self):
        self.collector = None
        self.cleaner = None
        self.storage = None
        self.visualizer = None

    def set_collector(self, collector):
        self.collector = collector
        return self

    def set_cleaner(self, cleaner):
        self.cleaner = cleaner
        return self

    def set_storage(self, storage):
        self.storage = storage
        return self

    def set_visualizer(self, visualizer):
        self.visualizer = visualizer
        return self

    def build(self):
        if not all([self.collector, self.cleaner, self.storage, self.visualizer]):
            raise ValueError("Tous les composants du pipeline doivent être définis.")
        return DataPipeline(
            collector=self.collector,
            cleaner=self.cleaner,
            storage=self.storage,
            visualizer=self.visualizer
        )
