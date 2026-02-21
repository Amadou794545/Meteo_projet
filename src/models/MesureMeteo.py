"""Domain model for a weather measurement."""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class MesureMeteo:  # pylint: disable=too-few-public-methods
    """Single weather measurement captured at a specific time."""

    temperature: float
    humidite: float
    pression: float
    pluie: float
    data_heure: datetime
