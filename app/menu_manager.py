class MenuManager:
    def __init__(self):
        pass

    def show_main_menu(self, default_city: str = "Toulouse", station_count: int = 0) -> str:
        """
        Display main menu.

        Args:
            default_city: Current city name
            station_count: Number of stations in current city

        Returns:
            str: User's choice
        """
        print("\n" + "=" * 50)
        print("🌤️  Weather Station App")
        print("=" * 50)
        print(f"📍 Location: {default_city} ({station_count} station(s))")
        print("\n1 - Manage Stations")
        print("2 - Show Weather")
        print("3 - Change Location")
        print("4 - Quit")
        print("=" * 50)
        return input("Choice > ").strip()

    def show_stations_menu(self) -> str:
        """
        Display stations management menu.

        Returns:
            str: User's choice
        """
        print("\n" + "-" * 50)
        print("📊 Station Management")
        print("-" * 50)
        print("1 - List All Stations")
        print("2 - Add Station")
        print("3 - Remove Station")
        print("4 - Back to Main Menu")
        print("-" * 50)
        return input("Choice > ").strip()