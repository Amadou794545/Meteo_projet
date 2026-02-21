import pytest
import pandas as pd
from src.cleaners.DataCleaner import DataCleaner
from src.collectors.APIDataCollector import APIDataCollector
from src.storage.CSVStorage import CSVStorage
from DataPipeline import DataPipeline
from unittest.mock import MagicMock
from utils.ListeChaine import LinkedList, Node



@pytest.fixture
def mock_collector():
    collector = MagicMock(spec=APIDataCollector)
    collector.collect_data.return_value = pd.DataFrame({
        "temperature_en_degre_c": [25.5, 26.0],
        "pluie": [0, 0.1],
        "humidite": [60, 65],
        "pression": [1013, 1012],
        "heure_de_paris": ["2023-10-01T12:00:00", "2023-10-01T13:00:00"]
    })
    return collector


@pytest.fixture
def mock_cleaner():
    cleaner = MagicMock(spec=DataCleaner)
    cleaner.clean_data.return_value = pd.DataFrame({
        "temperature_en_degre_c": [25.5, 26.0],
        "pluie": [0, 0.1],
        "humidite": [60, 65],
        "pression": [1013, 1012],
        "heure_de_paris": ["2023-10-01T12:00:00", "2023-10-01T13:00:00"]
    })
    return cleaner


@pytest.fixture
def mock_storage():
    storage = MagicMock(spec=CSVStorage)
    storage.save_data = MagicMock()
    return storage


@pytest.fixture
def mock_visualizer():
    visualizer = MagicMock()
    visualizer.visualize = MagicMock()
    return visualizer


def test_pipeline_run(mock_collector, mock_cleaner, mock_storage, mock_visualizer):
    pipeline = DataPipeline(
        collector=mock_collector,
        cleaner=mock_cleaner,
        storage=mock_storage,
        visualizer=mock_visualizer
    )

    result = pipeline.run()

    # Vérifie que les étapes du pipeline ont été appelées
    mock_collector.collect_data.assert_called_once()
    mock_cleaner.clean_data.assert_called_once()
    mock_storage.save_data.assert_called_once()
    mock_visualizer.visualize.assert_called_once()

    # Vérifie que le résultat est correct
    assert isinstance(result, pd.DataFrame)
    assert not result.empty
