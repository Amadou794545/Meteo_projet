from DataPipeline import DataPipeline
from src.cleaners.DataCleaner import DataCleaner
from src.collectors.APIDataCollector import APIDataCollector
from src.models.MesureMeteo import MesureMeteo
from src.models.StationMeteo import StationMeteo
from src.storage.CSVStorage import CSVStorage
from utils.APIClient import APIClient, STATIONS
import pandas as pd

# Interface pour choisir une station
print("Stations disponibles :")
for station in STATIONS.keys():
    print(f"- {station}")

station_choice = input("Entrez le nom de la station : ").strip().lower()
if station_choice not in STATIONS:
    print(f"Choix de station invalide : {station_choice}")
    exit(1)

# Initialisation du client API et du collecteur
client = APIClient(STATIONS[station_choice])
collector = APIDataCollector(client)
# rajouter une colonne station_name dans collector.collect_data


# Collecter les données
print("Collecte des données...")
data = collector.collect_data()

# Créer une station
print("Création de l'objet StationMeteo...")
station = [StationMeteo(
    id=rows['id'],
    name=station_choice,
    type=rows['type_de_station'],
    url=STATIONS[station_choice])

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

# Afficher les mesures
print("Affichage des mesures collectées :")
print(df_mesures.head())

# Initialisation du nettoyeur de données
print("Initialisation du DataCleaner...")
cleaner = DataCleaner(station_name=station_choice)

print("sauvegarde des données nettoyées...")
storage = CSVStorage(file_path="data/cleaned_data.csv", collector=collector)

# Initialiser et exécuter le pipeline
print("Exécution du pipeline de données...")

pipeline = DataPipeline(
    collector=collector,
    cleaner=cleaner,
    storage=storage,
    visualizer=None
)

df = pd.read_csv("data/cleaned_data.csv")
df.drop_duplicates(inplace=True)
df.to_csv("data/cleaned_data.csv", index=False)

result = pipeline.run(output_path="output.csv")
print("Résultat de la première ligne du pipeline :")
print(result)
