from abc import ABC, abstractmethod
import pandas as pd


class IDataCleaner(ABC):
    @abstractmethod
    def clean_data(self, data):
        pass