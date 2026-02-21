import argparse
import os
from queue import Queue

import pandas as pd

from DataPipeline import DataPipelineBuilder
from src.cleaners.DataCleaner import DataCleaner
from src.collectors.APIDataCollector import APIDataCollector
from src.models.MesureMeteo import MesureMeteo
from src.models.StationMeteo import StationMeteo
from src.storage.CSVStorage import CSVStorage
from src.visualizers.Visualizer import Visualizer
from utils.APIClient import APIClient, STATIONS
from utils.ListeChaine import LinkedList


def _parse_stations_arg(stations_value: str):
    return [name.strip() for name in stations_value.split(",") if name.strip()]


def _select_stations_from_cli():
    parser = argparse.ArgumentParser(
        description="Lancer le pipeline météo avec sélection des stations."
    )
    parser.add_argument(
        "--stations",
        type=_parse_stations_arg,
        help="Noms de stations séparés par des virgules (ex: montaudran,marengo).",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Traiter toutes les stations sans demander de saisie.",
    )

    args = parser.parse_args()
    available_station_names = list(STATIONS.keys())

    if args.all:
        return available_station_names

    if args.stations:
        invalid = [name for name in args.stations if name not in STATIONS]
        if invalid:
            parser.error(
                "Stations invalides: "
                + ", ".join(invalid)
                + ". Stations disponibles: "
                + ", ".join(available_station_names)
            )
        return args.stations

    print("Choisissez les stations à traiter :")
    for index, station_name in enumerate(available_station_names, start=1):
        print(f"  {index}. {station_name}")
    print("Saisissez les numéros séparés par des virgules (ex: 1,3) ou 'all'.")

    while True:
        user_input = input("Votre choix: ").strip().lower()

        if user_input == "all":
            return available_station_names

        raw_indices = [value.strip() for value in user_input.split(",") if value.strip()]

        if not raw_indices:
            print("⚠️ Aucun choix détecté, veuillez réessayer.")
            continue

        if not all(value.isdigit() for value in raw_indices):
            print("⚠️ Format invalide. Utilisez des numéros séparés par des virgules.")
            continue

        selected_indices = sorted({int(value) for value in raw_indices})
        if not all(1 <= index <= len(available_station_names) for index in selected_indices):
            print("⚠️ Un ou plusieurs numéros sont hors plage, veuillez réessayer.")
            continue

        return [available_station_names[index - 1] for index in selected_indices]


def main():
    selected_station_names = _select_stations_from_cli()

    stations_data = LinkedList()
    stations_queue = Queue()

    for station_name in selected_station_names:
        stations_queue.put((station_name, STATIONS[station_name]))

    while not stations_queue.empty():
        station_name, station_url = stations_queue.get()

        print(
            "----------------Collecte des données pour la station : "
            f"{station_name}----------------"
        )

        client = APIClient(station_url)
        collector = APIDataCollector(client)

        data = collector.collect_data()
        data['nom_station'] = station_name

        stations_data.append(station_name, data)

        print("Création de l'objet StationMeteo...")
        station = [
            StationMeteo(
                id=rows['id'],
                name=station_name,
                type=rows['type_de_station'],
                url=STATIONS[station_name],
            )
            for _, rows in data.iterrows()
        ]

        print("Transformation des données en objets MesureMeteo...")
        mesures = [
            MesureMeteo(
                temperature=row['temperature_en_degre_c'],
                pluie=row['pluie'],
                humidite=row['humidite'],
                pression=row['pression'],
                dataHeure=row['heure_de_paris'],
            )
            for _, row in data.iterrows()
        ]

        df_mesures = pd.DataFrame([vars(mesure) for mesure in mesures])

        print("Initialisation du DataCleaner...")
        cleaner = DataCleaner(station_name=station_name)

        print("Sauvegarde des données nettoyées...")
        storage = CSVStorage(file_path="data/cleaned_data.csv", collector=collector)

        print("Initialisation du visualizer...")
        visualizer = Visualizer()

        print("Exécution du pipeline de données...")

        pipeline_builder = DataPipelineBuilder()

        pipeline = (
            pipeline_builder
            .set_collector(collector)
            .set_cleaner(cleaner)
            .set_storage(storage)
            .set_visualizer(visualizer)
            .build()
        )

        result = pipeline.run()
        print("Résultat de la première ligne du pipeline :")
        print(result)

    file_path = "data/cleaned_data.csv"
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df.drop_duplicates(inplace=True)
        df.to_csv(file_path, index=False)
    else:
        print(f"⚠️ Le fichier '{file_path}' n'existe pas. Aucune opération effectuée.")
        return

    import pandas as pd

    print("---------------------✅ Pipeline exécuté pour les stations sélectionnées avec succès.------------------")


if __name__ == "__main__":
    main()
