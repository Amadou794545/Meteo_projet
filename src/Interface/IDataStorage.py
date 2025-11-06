from abc import ABC, abstractmethod


class IDataStorage(ABC):
    @abstractmethod
    def save_data(self, key: str, data: dict) -> None:
        pass

    @abstractmethod
    def load_data(self, key: str) -> dict:
        pass

    @abstractmethod
    def delete_data(self, key: str) -> None:
        pass
