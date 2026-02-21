"""Abstract visualizer contract."""

from abc import ABC, abstractmethod


class IDataVisualisation(ABC):  # pylint: disable=too-few-public-methods
    """Interface for data visualization components."""

    @abstractmethod
    def visualize(self, data):
        """Display or render data."""
