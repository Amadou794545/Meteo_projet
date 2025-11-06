from DataPipeline import DataPipeline
from src.collectors.APIDataCollector import APIDataCollector
from utils.APIClient import APIClient, STATIONS

# interface to choose station
print("Available stations:")
for station in STATIONS.keys():
    print(f"- {station}")

station_choice = input("Enter the station name: ").strip().lower()
if station_choice not in STATIONS:
    raise ValueError(f"Invalid station choice: {station_choice}")


client = APIClient(STATIONS[station_choice])
collector = APIDataCollector(client)

pipeline = DataPipeline(
    collector=collector,
    cleaner=None,
    storage=None,
    visualizer=None
)

print(pipeline.run(output_path="output.csv"))
