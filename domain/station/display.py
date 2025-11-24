from typing import Protocol
from domain.station.station import Station


class IStationDisplay(Protocol):

    def display(self, station: Station) -> str:
        ...


class DetailedStationDisplay:

    def display(self, station: Station) -> str:
        lines = [
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            f"📍 Station: {station.name}",
            f"🔗 API: {station.api_url}",
        ]

        if not station.has_data():
            lines.append("📊 Data: Not fetched yet (use refresh)")
        else:
            lines.append("📊 Weather Data:")
            data = station.data
            for key, value in data.items():
                lines.append(f"   • {key}: {value}")

        lines.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        return "\n".join(lines)


class CompactStationDisplay:
    def display(self, station: Station) -> str:
        status = "✅ Data available" if station.has_data() else "⏳ No data"
        return f"📍 {station.name} | {status}"


class TableStationDisplay:
    def display(self, station: Station) -> str:
        status = "✓" if station.has_data() else "✗"
        return f"| {station.name:20} | {status:^6} | {station.api_url:40} |"