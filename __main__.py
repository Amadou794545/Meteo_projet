import os
from DataPipeline import DataPipeline
from src.cleaners.DataCleaner import DataCleaner
from src.collectors.APIDataCollector import APIDataCollector
from src.models.MesureMeteo import MesureMeteo
from src.models.StationMeteo import StationMeteo
from src.storage.CSVStorage import CSVStorage
from src.visualizers.Visualizer import Visualizer
from utils.APIClient import APIClient, STATIONS
import pandas as pd

from utils.ListeChaine import LinkedList

if __name__ == "__main__":

    # Initialisation de la liste chaînée
    stations_data = LinkedList()

    # Parcourir toutes les stations disponibles
    for station_name, station_url in STATIONS.items():
        print(f"----------------Collecte des données pour la station : {station_name}----------------")

        # Initialisation du client API et du collecteur
        client = APIClient(station_url)
        collector = APIDataCollector(client)

        # Collecter les données
        data = collector.collect_data()
        data['nom_station'] = station_name

        # Ajouter les données à la liste chaînée
        stations_data.append(station_name, data)

        print("Création de l'objet StationMeteo...")
        station = [StationMeteo(
            id=rows['id'],
            name=station_name,
            type=rows['type_de_station'],
            url=STATIONS[station_name])

            for _, rows in data.iterrows()
        ]

        # Transformer les données en objets MesureMeteo
        print("Transformation des données en objets MesureMeteo...")
        mesures = [
            MesureMeteo(
                temperature=row['temperature_en_degre_c'],
                pluie=row['pluie'],
                humidite=row['humidite'],
                pression=row['pression'],
                dataHeure=row['heure_de_paris']
            )
            for _, row in data.iterrows()
        ]
        # convertir mesures en dataframe pandas
        df_mesures = pd.DataFrame([vars(mesure) for mesure in mesures])

        # Initialisation du nettoyeur de données
        print("Initialisation du DataCleaner...")
        cleaner = DataCleaner(station_name=station_name)

        print("sauvegarde des données nettoyées...")
        storage = CSVStorage(file_path="data/cleaned_data.csv", collector=collector)

        print("Initialisation du visualizer...")
        visualizer = Visualizer()
        # Initialiser et exécuter le pipeline
        print("Exécution du pipeline de données...")

        pipeline = DataPipeline(
            collector=collector,
            cleaner=cleaner,
            storage=storage,
            visualizer=visualizer
        )

        result = pipeline.run(output_path="output.csv")
        print("Résultat de la première ligne du pipeline :")
        print(result)


    # Créer une station

    file_path = "data/cleaned_data.csv"
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df.drop_duplicates(inplace=True)
        df.to_csv(file_path, index=False)
    else:
        print(f"⚠️ Le fichier '{file_path}' n'existe pas. Aucune opération effectuée.")

    print("---------------------✅ Pipeline exécuté pour toutes les stations avec succès.------------------")
