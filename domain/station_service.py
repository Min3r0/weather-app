from typing import Optional
from .station import Station


class StationService:
    """
    Service layer for station operations.
    Follows Single Responsibility: business logic for stations.
    Depends on abstractions (Dependency Inversion Principle).
    """

    def __init__(self, data_extractor=None):
        """
        Initialize station service.

        Args:
            data_extractor: DataExtract implementation (injected dependency)
        """
        self._data_extractor = data_extractor

    def refresh_station(self, station: Station) -> bool:
        """
        Refresh weather data for a station.

        Args:
            station: Station to refresh

        Returns:
            bool: True if refresh succeeded, False otherwise
        """
        if self._data_extractor is None:
            print(f"[StationService] No data extractor configured for '{station.name}'")
            station.data = {
                "status": "no_extractor",
                "message": "Data extractor not configured"
            }
            return False

        try:
            print(f"[StationService] Refreshing '{station.name}'... (stub)")
            # will be implemented in step 5 with real API call
            # data = self._data_extractor.get_data(station.api_url)

            # stub data for now
            station.data = {
                "status": "stub",
                "temperature": "N/A",
                "humidity": "N/A",
                "last_update": "stub_timestamp"
            }
            return True

        except Exception as e:
            print(f"[StationService] Error refreshing '{station.name}': {e}")
            station.data = {
                "status": "error",
                "message": str(e)
            }
            return False

    def validate_station_data(self, station: Station) -> tuple[bool, Optional[str]]:
        """
        Validate that station has valid data.

        Args:
            station: Station to validate

        Returns:
            tuple: (is_valid, error_message)
        """
        if not station.has_data():
            return False, "No data available"

        data = station.data

        if data.get("status") == "error":
            return False, f"Data error: {data.get('message', 'Unknown error')}"

        if data.get("status") == "no_extractor":
            return False, "Data extractor not configured"

        return True, None

    def clear_station_data(self, station: Station) -> None:
        """
        Clear weather data from a station.

        Args:
            station: Station to clear
        """
        station.data = None
        print(f"[StationService] Data cleared for '{station.name}'")


class StationFactory:
    """
    Factory for creating stations.
    Follows Open/Closed Principle: extensible without modification.
    """

    @staticmethod
    def create_station(name: str, api_url: str) -> Station:
        """
        Create a new station with validation.

        Args:
            name: Station name
            api_url: API URL

        Returns:
            Station: New station instance

        Raises:
            ValueError: If validation fails
        """
        # validation
        if not name or not name.strip():
            raise ValueError("Station name cannot be empty")

        if not api_url or not api_url.strip():
            raise ValueError("API URL cannot be empty")

        # could add more validation (URL format, etc.)

        return Station(name.strip(), api_url.strip())