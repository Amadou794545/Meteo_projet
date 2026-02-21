"""Domain model for a weather station."""

from dataclasses import dataclass


@dataclass
class StationMeteo:  # pylint: disable=too-few-public-methods
    """Metadata describing a weather station source."""

    station_id: str
    name: str
    station_type: str
    url: str
