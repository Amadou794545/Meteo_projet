from abc import ABC, abstractmethod
import pandas as pd


class IDataCleaner(ABC):
    @abstractmethod
    def clean_data(self, data):
        pass

    @abstractmethod
    def _remove_doublons(self, data):
        pass

    @abstractmethod
    def _remove_missing_values(self, data):
        pass

    @abstractmethod
    def _filter_outliers(self, data):
        pass

    @abstractmethod
    def _separate_date_time(self, data):
        pass