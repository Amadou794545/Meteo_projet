"""Abstract cleaner contract."""

from abc import ABC, abstractmethod


class IDataCleaner(ABC):  # pylint: disable=too-few-public-methods
    """Interface for weather data cleaning components."""

    @abstractmethod
    def clean_data(self, data):
        """Run the full cleaning process on the given data."""

    @abstractmethod
    def _remove_doublons(self, data):
        """Remove duplicate records."""

    @abstractmethod
    def _remove_missing_values(self, data):
        """Remove records with missing values."""

    @abstractmethod
    def _filter_outliers(self, data):
        """Filter out anomalous records."""

    @abstractmethod
    def _separate_date_time(self, data):
        """Split datetime information into date and time columns."""
