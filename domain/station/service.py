class StationService:
    """Service métier pour gérer la logique d’une station météo."""

    @staticmethod
    def validate_data(station) -> bool:
        """Vérifie la cohérence des données d’une station."""
        if not station.data:
            return False
        required_keys = {"temperature_en_degre_c", "humidite", "pression"}
        for item in station.data:
            if not required_keys.issubset(item.keys()):
                return False
        return True

    @staticmethod
    def clear_data(station):
        """Efface les données d’une station."""
        station.clear_data()

    @staticmethod
    def get_summary(station) -> str:
        """Retourne un résumé court de la station."""
        if not station.data:
            return f"{station.name}: aucune donnée disponible."
        last = station.data[-1]
        return f"{station.name}: 🌡️ {last['temperature_en_degre_c']}°C, 💧 {last['humidite']}%, ⏱️ {last['heure_de_paris']}"
