from datetime import datetime
from typing import Any
from core.data_extractor import DataExtract


class Station:
    """Représente une station météo individuelle."""

    def __init__(self, name: str, api_url: str, data_extractor: DataExtract):
        self.name = name
        self.api_url = api_url
        self.data_extractor = data_extractor
        self.data: list[dict[str, Any]] = []

    # -----------------------
    # MÉTHODES MÉTIER
    # -----------------------
    def refresh_data(self):
        """Actualise les données météo depuis l’API."""
        new_data = self.data_extractor.get_data(self.api_url)
        if new_data:
            self.data = new_data

    def clear_data(self):
        """Efface toutes les données météo stockées."""
        self.data.clear()

    # -----------------------
    # UTILITAIRES
    # -----------------------
    def to_dict(self) -> dict:
        """Sérialise la station pour la sauvegarde JSON."""
        return {
            "name": self.name,
            "api_url": self.api_url,
            "data": self.data,
        }

    @classmethod
    def from_dict(cls, data: dict, data_extractor: DataExtract):
        """Reconstruit une station depuis un dict JSON."""
        station = cls(data["name"], data["api_url"], data_extractor)
        station.data = data.get("data", [])
        return station
