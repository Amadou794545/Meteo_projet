from abc import ABC, abstractmethod

import pandas as pd


class IDataStorage(ABC):
    @abstractmethod
    def save_data(self,data: pd.DataFrame) -> None:
        pass

    @abstractmethod
    def load_data(self, key: str) -> dict:
        pass

    @abstractmethod
    def delete_data(self, key: str) -> None:
        pass

