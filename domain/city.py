from typing import Optional
from .station_manager import StationManager


class City:
    """
    Represents a city containing weather stations.
    Follows Single Responsibility Principle: manages city-level data.
    """

    def __init__(self, name: str, country=None):
        """
        Initialize a city.

        Args:
            name: City name (e.g., "Toulouse")
            country: Country object this city belongs to
        """
        self._name = name
        self._country = country
        self._station_manager: Optional[StationManager] = None

    @property
    def name(self) -> str:
        """Get city name."""
        return self._name

    @property
    def country(self):
        """Get country this city belongs to."""
        return self._country

    @property
    def station_manager(self) -> Optional[StationManager]:
        """Get station manager for this city."""
        return self._station_manager

    def set_station_manager(self, manager: StationManager) -> None:
        """
        Set the station manager for this city.
        Allows dependency injection (Dependency Inversion Principle).

        Args:
            manager: StationManager instance
        """
        self._station_manager = manager

    def __str__(self) -> str:
        country_name = self._country.name if self._country else "Unknown"
        station_count = self._station_manager.count() if self._station_manager else 0
        return f"City: {self._name} ({country_name}) - {station_count} station(s)"