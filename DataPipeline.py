"""Pipeline orchestration classes for the weather processing flow."""

from src.cleaners.DataCleaner import DataCleaner
from src.collectors.APIDataCollector import APIDataCollector
from src.storage.CSVStorage import CSVStorage


class DataPipeline:  # pylint: disable=too-few-public-methods
    """Run collector, cleaner, storage and visualization in sequence."""

    def __init__(
        self,
        collector: APIDataCollector,
        cleaner: DataCleaner,
        storage: CSVStorage,
        visualizer,
    ):
        self.collector = collector
        self.cleaner = cleaner
        self.storage = storage
        self.visualizer = visualizer

    def run(self):
        """Execute the pipeline and return the first row for verification."""
        data = self.collector.collect_data()
        data = self.cleaner.clean_data(data)
        self.storage.save_data(data=data)
        self.visualizer.visualize(data)
        return data.head(1)


class DataPipelineBuilder:
    """Builder used to assemble a complete :class:`DataPipeline`."""

    def __init__(self):
        self.collector = None
        self.cleaner = None
        self.storage = None
        self.visualizer = None

    def set_collector(self, collector):
        """Set the collector component."""
        self.collector = collector
        return self

    def set_cleaner(self, cleaner):
        """Set the cleaner component."""
        self.cleaner = cleaner
        return self

    def set_storage(self, storage):
        """Set the storage component."""
        self.storage = storage
        return self

    def set_visualizer(self, visualizer):
        """Set the visualizer component."""
        self.visualizer = visualizer
        return self

    def build(self):
        """Validate and build a :class:`DataPipeline` instance."""
        if not all([self.collector, self.cleaner, self.storage, self.visualizer]):
            raise ValueError("Tous les composants du pipeline doivent être définis.")
        return DataPipeline(
            collector=self.collector,
            cleaner=self.cleaner,
            storage=self.storage,
            visualizer=self.visualizer,
        )
