"""Collector implementation that fetches weather records from an API."""

import pandas as pd
import requests

from src.Interface.IDataCollector import IDataCollector


class APIDataCollector(IDataCollector):  # pylint: disable=too-few-public-methods
    """Retrieve and normalize data from a remote HTTP endpoint."""

    def __init__(self, api_client):
        self.api_client = api_client

    def collect_data(self):
        """Call the API endpoint and return a pandas DataFrame."""
        try:
            response = requests.get(
                self.api_client.base_url,
                params=self.api_client.params,
                timeout=15,
            )
            response.raise_for_status()
            data = response.json()

            if "results" not in data:
                raise ValueError("Missing 'results' in API response")

            return pd.DataFrame(data["results"])

        except requests.exceptions.RequestException as error:
            raise RuntimeError(f"API request failed: {error}") from error
