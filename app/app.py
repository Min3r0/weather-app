from interface.cli_manager import CLIManager
from domain.station.manager import StationManager
from domain.country import Country
from domain.city import City
from core.data_extractor import ViaAPI
from domain.station.service import StationService

class App:
    def __init__(self):
        self.cli = CLIManager()
        self.extractor = ViaAPI()
        self.service = StationService(self.extractor)
        self.country = Country("France")
        self.city = City("Toulouse", self.country)
        self.manager = StationManager(self.service)

    def run(self):
        self.cli.display("🌤️ Weather Station App - CLI Version")
        while True:
            choice = self.cli.display_menu("Main Menu", [
                "List stations",
                "Add station",
                "Refresh all",
                "Quit"
            ])
            if choice == 1:
                self.cli.display_station_list(self.manager.list_stations())
            elif choice == 2:
                name = self.cli.input_text("Station name: ")
                url = self.cli.input_text("API URL: ")
                self.cli.display(self.manager.add_station(name, url))
            elif choice == 3:
                self.cli.display(self.manager.refresh_all_stations())
            elif choice == 4:
                self.cli.display("👋 Bye!")
                break
            else:
                self.cli.display("❌ Invalid choice.")
