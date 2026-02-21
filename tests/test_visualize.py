import pytest
import pandas as pd
from src.visualizers.Visualizer import Visualizer


@pytest.fixture
def visualizer():
    """Fixture pour initialiser le visualiseur avant chaque test."""
    return Visualizer()


@pytest.fixture
def sample_data():
    """Fixture fournissant un DataFrame de test."""
    return pd.DataFrame({
        "Station": ["Paris"],
        "Temp": [20.5],
        "Humidité": [50]
    })


def test_visualize_success(visualizer, sample_data, capsys):
    """Vérifie que la visualisation affiche correctement les données de la première ligne."""
    visualizer.visualize(sample_data)

    # Capture la sortie du print
    captured = capsys.readouterr()

    # Vérifications
    assert "Station: Paris" in captured.out
    assert "Temp: 20.5" in captured.out
    assert "Humidité: 50" in captured.out


def test_visualize_empty_df(visualizer):
    """Vérifie qu'une exception est levée si le DataFrame est vide."""
    empty_df = pd.DataFrame()
    with pytest.raises(ValueError, match="Le DataFrame fourni est vide ou invalide."):
        visualizer.visualize(empty_df)


def test_visualize_none(visualizer):
    """Vérifie qu'une exception est levée si la donnée est None."""
    with pytest.raises(ValueError, match="Le DataFrame fourni est vide ou invalide."):
        visualizer.visualize(None)