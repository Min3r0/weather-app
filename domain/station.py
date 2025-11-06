from typing import Optional, Dict, Any


class Station:
    """
    Represents a weather station (pure data model).
    Follows Single Responsibility Principle: only holds station data.
    No display logic, no refresh logic - just data management.
    """

    def __init__(self, name: str, api_url: str):
        """
        Initialize a weather station.

        Args:
            name: Station name (e.g., "Capitole")
            api_url: API endpoint to fetch weather data
        """
        self._name = name
        self._api_url = api_url
        self._data: Optional[Dict[str, Any]] = None

    @property
    def name(self) -> str:
        """Get station name."""
        return self._name

    @property
    def api_url(self) -> str:
        """Get API URL."""
        return self._api_url

    @property
    def data(self) -> Optional[Dict[str, Any]]:
        """Get current weather data."""
        return self._data

    @data.setter
    def data(self, value: Optional[Dict[str, Any]]) -> None:
        """Set weather data."""
        self._data = value

    def has_data(self) -> bool:
        """
        Check if station has weather data.

        Returns:
            bool: True if data is available
        """
        return self._data is not None

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert station to dictionary (for JSON serialization).

        Returns:
            dict: Station data as dictionary
        """
        return {
            "name": self._name,
            "api_url": self._api_url,
            "data": self._data
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Station':
        """
        Create Station from dictionary (for JSON deserialization).

        Args:
            data: Dictionary containing station data

        Returns:
            Station: New Station instance
        """
        station = cls(
            name=data["name"],
            api_url=data["api_url"]
        )
        station._data = data.get("data")
        return station

    def __eq__(self, other) -> bool:
        """Compare stations by name."""
        if not isinstance(other, Station):
            return False
        return self._name.lower() == other._name.lower()

    def __hash__(self) -> int:
        """Hash based on name."""
        return hash(self._name.lower())

    def __str__(self) -> str:
        """Simple string representation."""
        return f"Station({self._name})"