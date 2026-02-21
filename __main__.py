"""Entry point for the weather data pipeline CLI."""

import argparse
import os
from queue import Queue

from utils.APIClient import STATIONS


def _parse_args():
    """Parse CLI options for station selection."""
    parser = argparse.ArgumentParser(description="Pipeline météo Toulouse Métropole")
    parser.add_argument(
        "--stations",
        nargs="+",
        default=["all"],
        help=(
            "Liste des stations à traiter (séparées par des espaces). "
            "Exemple: --stations montaudran pech-david. "
            "Utiliser 'all' pour toutes les stations."
        ),
    )
    parser.add_argument(
        "--list-stations",
        action="store_true",
        help="Affiche les stations disponibles puis quitte.",
    )
    return parser.parse_args()


def _select_stations(selected_station_names):
    """Validate and return selected stations as a name/url mapping."""
    available_station_names = set(STATIONS.keys())

    if "all" in selected_station_names:
        return STATIONS

    invalid_station_names = [
        station_name
        for station_name in selected_station_names
        if station_name not in available_station_names
    ]

    if invalid_station_names:
        raise ValueError(
            "Stations inconnues: "
            f"{', '.join(invalid_station_names)}. "
            f"Stations disponibles: {', '.join(STATIONS.keys())}"
        )

    return {
        station_name: STATIONS[station_name]
        for station_name in selected_station_names
    }


def _process_stations(selected_stations):
    """Run the existing pipeline for each selected station."""
    from DataPipeline import DataPipelineBuilder
    from src.cleaners.DataCleaner import DataCleaner
    from src.collectors.APIDataCollector import APIDataCollector
    from src.storage.CSVStorage import CSVStorage
    from src.visualizers.Visualizer import Visualizer
    from utils.APIClient import APIClient
    from utils.ListeChaine import LinkedList

    stations_data = LinkedList()
    stations_queue = Queue()

    for station_name, station_url in selected_stations.items():
        stations_queue.put((station_name, station_url))

    while not stations_queue.empty():
        station_name, station_url = stations_queue.get()

        print(
            "----------------Collecte des données pour la station : "
            f"{station_name}----------------"
        )

        client = APIClient(station_url)
        collector = APIDataCollector(client)

        data = collector.collect_data()
        data["nom_station"] = station_name
        stations_data.append(station_name, data)

        print("Initialisation du DataCleaner...")
        cleaner = DataCleaner(station_name=station_name)

        print("Sauvegarde des données nettoyées...")
        storage = CSVStorage(file_path="data/cleaned_data.csv", collector=collector)

        print("Initialisation du visualizer...")
        visualizer = Visualizer()

        print("Exécution du pipeline de données...")
        pipeline = (
            DataPipelineBuilder()
            .set_collector(collector)
            .set_cleaner(cleaner)
            .set_storage(storage)
            .set_visualizer(visualizer)
            .build()
        )

        result = pipeline.run()
        print("Résultat de la première ligne du pipeline :")
        print(result)


def _deduplicate_output_csv(file_path="data/cleaned_data.csv"):
    """Drop duplicate rows from the target CSV file if it exists."""
    if not os.path.exists(file_path):
        print(f"⚠️ Le fichier '{file_path}' n'existe pas. Aucune opération effectuée.")
        return

    import pandas as pd

    dataframe = pd.read_csv(file_path)
    dataframe.drop_duplicates(inplace=True)
    dataframe.to_csv(file_path, index=False)


def main():
    """CLI main function."""
    args = _parse_args()

    if args.list_stations:
        print("Stations disponibles:")
        for station_name in STATIONS.keys():
            print(f"- {station_name}")
        return

    selected_station_names = [station.lower() for station in args.stations]

    try:
        selected_stations = _select_stations(selected_station_names)
    except ValueError as error:
        raise SystemExit(f"❌ {error}") from error

    _process_stations(selected_stations)
    _deduplicate_output_csv()

    print(
        "---------------------✅ Pipeline exécuté pour toutes les stations "
        "avec succès.------------------"
    )


if __name__ == "__main__":
    main()
