"""Abstract storage contract."""

from abc import ABC, abstractmethod

import pandas as pd


class IDataStorage(ABC):
    """Interface for data persistence services."""

    @abstractmethod
    def save_data(self, data: pd.DataFrame) -> None:
        """Persist cleaned data."""

    @abstractmethod
    def load_data(self, key: str) -> pd.DataFrame:
        """Load data from storage."""

    @abstractmethod
    def delete_data(self, key: str) -> None:
        """Delete data from storage."""
