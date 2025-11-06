import pandas as pd
import requests
from src.Interface.IDataCollector import IDataCollector


class APIDataCollector(IDataCollector):

    def __init__(self, api_client):
        self.api_client = api_client

    def collect_data(self):
        try:
            response = requests.get(
                self.api_client.base_url,
                params=self.api_client.params
            )
            response.raise_for_status()

            data = response.json()

            # Vérifier la présence de 'results'
            if 'results' not in data:
                raise ValueError("Missing 'results' in API response")

            df = pd.DataFrame(data['results'])

            return df

        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"API request failed: {e}")

