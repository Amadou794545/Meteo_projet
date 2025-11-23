from src.collectors.APIDataCollector import APIDataCollector



class DataPipeline:
    def __init__(self, collector: APIDataCollector, cleaner, storage, visualizer):
        self.collector = collector
        self.cleaner = cleaner
        self.storage = storage
        self.visualizer = visualizer

    def run(self, output_path):
        # Étape 1 : Collecte
        data = self.collector.collect_data()# Exemple de mappage des données récupérées



        # Étape 2 : Nettoyage
        # à faire
        #data = self.cleaner.clean(data)

        # Étape 3 : Sauvegarde
        #self.storage.save(data, output_path)

        # Étape 4 : Visualisation
        # à faire
        #self.visualizer.visualize(data)

        #renvoie la première ligne du dataframe pour vérification
        return data.head(1)

        print("✅ Pipeline exécuté avec succès.")
