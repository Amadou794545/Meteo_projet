from abc import ABC, abstractmethod
import pandas as pd


class IDataVisualisation(ABC):
    @abstractmethod
    def visualize(self, data):
        pass