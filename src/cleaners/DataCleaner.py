"""Data cleaning utilities for weather measurements."""

import pandas as pd

from src.Interface.IDataCleaner import IDataCleaner


class DataCleaner(IDataCleaner):  # pylint: disable=too-few-public-methods
    """Clean weather records by removing missing values and anomalies."""

    def __init__(self, temperature_range=(-10, 50), station_name="unknown_station"):
        self.temperature_min, self.temperature_max = temperature_range
        self.station_name = station_name

    def clean_data(self, data) -> pd.DataFrame:
        """Apply all cleaning steps to an input DataFrame."""
        if data is None or data.empty:
            raise ValueError("Le DataFrame fourni est vide ou invalide.")

        data["nom_station"] = self.station_name
        data = self._remove_missing_values(data)
        data = self._filter_outliers(data)
        data = self._remove_doublons(data)
        data = self._separate_date_time(data)
        return data

    def _remove_doublons(self, data):
        """Remove duplicate rows by timestamp and station."""
        return data.drop_duplicates(subset=["heure_de_paris", "nom_station"])

    def _remove_missing_values(self, data):
        """Drop rows containing missing values."""
        return data.dropna()

    def _filter_outliers(self, data):
        """Keep records where temperature is within accepted range."""
        return data[
            (data["temperature_en_degre_c"] >= self.temperature_min)
            & (data["temperature_en_degre_c"] <= self.temperature_max)
        ]

    def _separate_date_time(self, data):
        """Split the datetime column into date and time columns."""
        data["date"] = pd.to_datetime(data["heure_de_paris"]).dt.date
        data["time"] = pd.to_datetime(data["heure_de_paris"]).dt.time
        return data
