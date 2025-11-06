from .menu_manager import MenuManager
from .config_manager import ConfigManager
from domain import (
    Country, City, StationManager, StationService,
    DetailedStationDisplay, CompactStationDisplay
)


class App:
    def __init__(self):
        self.config = ConfigManager()
        self.menu = MenuManager()

        # initialize services (dependency injection)
        self.station_service = StationService()  # will inject data_extractor in step 3
        self.detailed_display = DetailedStationDisplay()
        self.compact_display = CompactStationDisplay()

        # initialize domain models
        self.current_country = Country(self.config.config.get("default_country", "France"))
        self.current_city = City(self.config.get_default_city(), self.current_country)

        # create station manager with injected service
        station_manager = StationManager(self.station_service)
        self.current_city.set_station_manager(station_manager)
        self.current_country.add_city(self.current_city)

        # add some example stations for testing
        self._init_example_stations()

        self.running = True

    def _init_example_stations(self):
        """Add example stations for testing (temporary)."""
        manager = self.current_city.station_manager
        try:
            manager.add_station("Capitole", "https://api.example.com/toulouse/capitole")
            manager.add_station("Jean Jaurès", "https://api.example.com/toulouse/jean-jaures")
        except ValueError as e:
            print(f"Warning: {e}")

    def run(self):
        while self.running:
            choice = self.menu.show_main_menu(
                default_city=self.current_city.name,
                station_count=self.current_city.station_manager.count()
            )

            if choice == "1":
                self._show_stations_menu()
            elif choice == "2":
                self._show_weather()
            elif choice == "3":
                print("\n[Feature] Change location — coming soon.")
                input("Press Enter to continue...")
            elif choice == "4":
                print("Bye 👋")
                self.running = False
            else:
                print("❌ Invalid choice, try again.")

    def _show_stations_menu(self):
        """Show stations submenu."""
        while True:
            choice = self.menu.show_stations_menu()

            if choice == "1":
                self._list_stations()
            elif choice == "2":
                self._add_station()
            elif choice == "3":
                self._remove_station()
            elif choice == "4":
                break
            else:
                print("❌ Invalid choice, try again.")

    def _list_stations(self):
        """Display all stations using compact display."""
        manager = self.current_city.station_manager
        stations = manager.list_stations()

        print(f"\n{'=' * 50}")
        print(f"📍 Stations in {self.current_city.name}")
        print(f"{'=' * 50}")

        if not stations:
            print("No stations available yet.")
        else:
            for i, station in enumerate(stations, 1):
                # use compact display strategy
                print(f"{i}. {self.compact_display.display(station)}")

        input("\nPress Enter to continue...")

    def _add_station(self):
        """Add a new station interactively."""
        print("\n--- Add New Station ---")
        name = input("Station name: ").strip()
        api_url = input("API URL: ").strip()

        if not name or not api_url:
            print("❌ Name and URL cannot be empty.")
            input("Press Enter to continue...")
            return

        try:
            manager = self.current_city.station_manager
            manager.add_station(name, api_url)
            input("Press Enter to continue...")
        except ValueError as e:
            print(f"❌ Error: {e}")
            input("Press Enter to continue...")

    def _remove_station(self):
        """Remove a station interactively."""
        manager = self.current_city.station_manager
        stations = manager.list_stations()

        if not stations:
            print("\n❌ No stations to remove.")
            input("Press Enter to continue...")
            return

        print("\n--- Remove Station ---")
        for i, station in enumerate(stations, 1):
            print(f"{i}. {station.name}")

        choice = input("\nEnter station number to remove (or 0 to cancel): ").strip()

        try:
            idx = int(choice)
            if idx == 0:
                return
            if 1 <= idx <= len(stations):
                station = stations[idx - 1]
                confirm = input(f"⚠️  Remove '{station.name}'? (y/n): ").strip().lower()
                if confirm == 'y':
                    manager.remove_station(station.name)
            else:
                print("❌ Invalid number.")
        except ValueError:
            print("❌ Invalid input.")

        input("Press Enter to continue...")

    def _show_weather(self):
        """Show weather for a selected station using detailed display."""
        manager = self.current_city.station_manager
        stations = manager.list_stations()

        if not stations:
            print("\n❌ No stations available.")
            input("Press Enter to continue...")
            return

        print("\n--- Select Station ---")
        for i, station in enumerate(stations, 1):
            print(f"{i}. {station.name}")

        choice = input("\nEnter station number (or 0 to cancel): ").strip()

        try:
            idx = int(choice)
            if idx == 0:
                return
            if 1 <= idx <= len(stations):
                station = stations[idx - 1]
                # refresh via manager (which delegates to service)
                manager.refresh_station(station)
                # display using detailed display strategy
                print(f"\n{self.detailed_display.display(station)}")
            else:
                print("❌ Invalid number.")
        except ValueError:
            print("❌ Invalid input.")

        input("\nPress Enter to continue...")