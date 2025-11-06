from typing import List, Optional
from .station import Station
from .station_service import StationFactory, StationService


class StationManager:
    """
    Manages a collection of weather stations.
    Follows Single Responsibility: only manages station collection.
    Delegates business logic to StationService (SRP).
    """

    def __init__(self, station_service: Optional[StationService] = None):
        """
        Initialize station manager.

        Args:
            station_service: Service for station operations (dependency injection)
        """
        self._stations: List[Station] = []
        self._station_service = station_service or StationService()
        self._factory = StationFactory()

    def add_station(self, name: str, api_url: str) -> Station:
        """
        Add a new station to the manager.

        Args:
            name: Station name
            api_url: API endpoint URL

        Returns:
            Station: The newly created station

        Raises:
            ValueError: If station with same name already exists or validation fails
        """
        # check if station already exists
        if self.get_station_by_name(name) is not None:
            raise ValueError(f"Station '{name}' already exists")

        # use factory to create station (with validation)
        station = self._factory.create_station(name, api_url)
        self._stations.append(station)
        print(f"✅ Station '{name}' added successfully")
        return station

    def remove_station(self, name: str) -> bool:
        """
        Remove a station by name.

        Args:
            name: Station name to remove

        Returns:
            bool: True if removed, False if not found
        """
        station = self.get_station_by_name(name)
        if station is None:
            return False

        self._stations.remove(station)
        print(f"🗑️  Station '{name}' removed")
        return True

    def get_station_by_name(self, name: str) -> Optional[Station]:
        """
        Get a station by its name.

        Args:
            name: Station name to search

        Returns:
            Optional[Station]: The station if found, None otherwise
        """
        for station in self._stations:
            if station.name.lower() == name.lower():
                return station
        return None

    def list_stations(self) -> List[Station]:
        """
        Get all stations.

        Returns:
            List[Station]: List of all stations
        """
        return self._stations.copy()

    def get_station_names(self) -> List[str]:
        """
        Get list of all station names.

        Returns:
            List[str]: List of station names
        """
        return [station.name for station in self._stations]

    def count(self) -> int:
        """
        Get number of stations.

        Returns:
            int: Number of stations managed
        """
        return len(self._stations)

    def refresh_station(self, station: Station) -> bool:
        """
        Refresh a station's data.
        Delegates to StationService.

        Args:
            station: Station to refresh

        Returns:
            bool: True if refresh succeeded
        """
        return self._station_service.refresh_station(station)

    def refresh_all_stations(self) -> int:
        """
        Refresh all stations.

        Returns:
            int: Number of successfully refreshed stations
        """
        success_count = 0
        for station in self._stations:
            if self._station_service.refresh_station(station):
                success_count += 1

        print(f"✅ Refreshed {success_count}/{len(self._stations)} stations")
        return success_count