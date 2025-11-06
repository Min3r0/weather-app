from typing import List, Optional
from .city import City


class Country:
    """
    Represents a country containing cities.
    Follows Single Responsibility Principle: manages country-level data.
    """

    def __init__(self, name: str):
        """
        Initialize a country.

        Args:
            name: Country name (e.g., "France")
        """
        self._name = name
        self._cities: List[City] = []

    @property
    def name(self) -> str:
        """Get country name."""
        return self._name

    @property
    def cities(self) -> List[City]:
        """Get list of cities in this country."""
        return self._cities.copy()

    def add_city(self, city: City) -> None:
        """
        Add a city to this country.

        Args:
            city: City instance to add

        Raises:
            ValueError: If city with same name already exists
        """
        if self.get_city_by_name(city.name) is not None:
            raise ValueError(f"City '{city.name}' already exists in {self._name}")

        self._cities.append(city)
        print(f"✅ City '{city.name}' added to {self._name}")

    def get_city_by_name(self, name: str) -> Optional[City]:
        """
        Get a city by its name.

        Args:
            name: City name to search

        Returns:
            Optional[City]: The city if found, None otherwise
        """
        for city in self._cities:
            if city.name.lower() == name.lower():
                return city
        return None

    def get_city_names(self) -> List[str]:
        """
        Get list of all city names.

        Returns:
            List[str]: List of city names
        """
        return [city.name for city in self._cities]

    def __str__(self) -> str:
        return f"Country: {self._name} - {len(self._cities)} city/cities"