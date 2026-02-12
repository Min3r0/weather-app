"""
Modèles pour les localisations avec héritage.
Principe SOLID: Open/Closed - ouvert à l'extension, fermé à la modification.
"""
from typing import List
from abc import ABC, abstractmethod


class Location(ABC):
    """Classe abstraite de base pour toutes les localisations."""

    def __init__(self, identifier: str, nom: str):
        """
        Initialise une localisation.

        Args:
            identifier: Identifiant unique de la localisation
            nom: Nom de la localisation
        """
        self._id = identifier
        self._nom = nom

    @property
    def id(self) -> str:
        """Retourne l'identifiant de la localisation."""
        return self._id

    @property
    def nom(self) -> str:
        """Retourne le nom de la localisation."""
        return self._nom

    @abstractmethod
    def get_info(self) -> str:
        """Retourne les informations de la localisation."""
        raise NotImplementedError


class Pays(Location):
    """Représente un pays."""

    def __init__(self, identifier: str, nom: str):
        """
        Initialise un pays.

        Args:
            identifier: Identifiant unique du pays
            nom: Nom du pays
        """
        super().__init__(identifier, nom)
        self._villes: List['Ville'] = []

    def add_ville(self, ville: 'Ville') -> None:
        """Ajoute une ville au pays."""
        if ville not in self._villes:
            self._villes.append(ville)

    def get_villes(self) -> List['Ville']:
        """Retourne la liste des villes du pays."""
        return self._villes.copy()

    def get_info(self) -> str:
        """Retourne les informations du pays."""
        return f"Pays: {self.nom} (ID: {self.id}) - {len(self._villes)} ville(s)"


class Ville(Location):
    """Représente une ville, hérite de Location."""

    def __init__(self, identifier: str, nom: str, pays: Pays):
        """
        Initialise une ville.

        Args:
            identifier: Identifiant unique de la ville
            nom: Nom de la ville
            pays: Pays auquel appartient la ville
        """
        super().__init__(identifier, nom)
        self._pays = pays
        self._stations: List['Station'] = []
        pays.add_ville(self)

    @property
    def pays(self) -> Pays:
        """Retourne le pays de la ville."""
        return self._pays

    def add_station(self, station: 'Station') -> None:
        """Ajoute une station météo à la ville."""
        if station not in self._stations:
            self._stations.append(station)

    def get_stations(self) -> List['Station']:
        """Retourne la liste des stations de la ville."""
        return self._stations.copy()

    def get_info(self) -> str:
        """Retourne les informations de la ville."""
        return f"Ville: {self.nom} (Pays: {self._pays.nom}) - {len(self._stations)} station(s)"


class Station(Location):
    """Représente une station météo, hérite de Location."""

    def __init__(self, identifier: str, nom: str, ville: Ville, api_url: str):
        """
        Initialise une station météo.

        Args:
            identifier: Identifiant unique de la station
            nom: Nom de la station
            ville: Ville où se trouve la station
            api_url: URL de l'API pour récupérer les données
        """
        super().__init__(identifier, nom)
        self._ville = ville
        self._api_url = api_url
        self._measurements: List = []
        ville.add_station(self)

    @property
    def ville(self) -> Ville:
        """Retourne la ville de la station."""
        return self._ville

    @property
    def api_url(self) -> str:
        """Retourne l'URL de l'API de la station."""
        return self._api_url

    @api_url.setter
    def api_url(self, new_url: str) -> None:
        """Modifie l'URL de l'API."""
        self._api_url = new_url

    def add_measurement(self, measurement) -> None:
        """Ajoute une mesure météo."""
        self._measurements.append(measurement)

    def get_measurements(self) -> List:
        """Retourne la liste des mesures."""
        return self._measurements.copy()

    def clear_measurements(self) -> None:
        """Efface toutes les mesures."""
        self._measurements.clear()

    def get_info(self) -> str:
        """Retourne les informations de la station."""
        return (f"Station: {self.nom} (Ville: {self._ville.nom}, "
                f"Pays: {self._ville.pays.nom}) - {len(self._measurements)} mesure(s)")
