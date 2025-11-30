from src.Interface.IdataVisualisation import IDataVisualisation


class Visualizer(IDataVisualisation):
    def __init__(self):
        pass

    # methode qui affiche la derniere ligne du dataframe colonne par colonne
    def visualize(self, data):
        if data is None or data.empty:
            raise ValueError("Le DataFrame fourni est vide ou invalide.")
        last_row = data.iloc[0]
        for column, value in last_row.items():
            print(f"{column}: {value}")
