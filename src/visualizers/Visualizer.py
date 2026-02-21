"""Console visualizer implementation."""

from src.Interface.IdataVisualisation import IDataVisualisation


class Visualizer(IDataVisualisation):  # pylint: disable=too-few-public-methods
    """Display the latest weather record in the console."""

    def visualize(self, data):
        """Print each column/value from the latest row in the DataFrame."""
        if data is None or data.empty:
            raise ValueError("Le DataFrame fourni est vide ou invalide.")
        last_row = data.iloc[0]
        for column, value in last_row.items():
            print(f"{column}: {value}")
