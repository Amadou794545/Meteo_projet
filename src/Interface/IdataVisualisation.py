from abc import ABC, abstractmethod
import pandas as pd


class IDataVisualisation(ABC):
    @abstractmethod
    def render(self, data):
        pass