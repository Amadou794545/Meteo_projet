from abc import ABC, abstractmethod
import pandas as pd


class IDataCollector(ABC):
    @abstractmethod
    def collect_data(self):
        pass

