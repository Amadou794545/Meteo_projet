"""Abstract collector contract."""

from abc import ABC, abstractmethod


class IDataCollector(ABC):  # pylint: disable=too-few-public-methods
    """Interface for data collector components."""

    @abstractmethod
    def collect_data(self):
        """Collect data and return it in a concrete representation."""
