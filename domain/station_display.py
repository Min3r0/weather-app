from typing import Protocol
from .station import Station


class IStationDisplay(Protocol):
    """
    Protocol for station display strategies.
    Allows different display formats (Liskov Substitution Principle).
    """

    def display(self, station: Station) -> str:
        """
        Display station information.

        Args:
            station: Station to display

        Returns:
            str: Formatted display string
        """
        ...


class DetailedStationDisplay:
    """
    Detailed display format for stations.
    Follows Single Responsibility: only handles detailed formatting.
    """

    def display(self, station: Station) -> str:
        """
        Display station with full details.

        Args:
            station: Station to display

        Returns:
            str: Formatted display string
        """
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
    """
    Compact display format for stations.
    Useful for lists or summaries.
    """

    def display(self, station: Station) -> str:
        """
        Display station in compact format.

        Args:
            station: Station to display

        Returns:
            str: Compact formatted string
        """
        status = "✅ Data available" if station.has_data() else "⏳ No data"
        return f"📍 {station.name} | {status}"


class TableStationDisplay:
    """
    Table-style display format for multiple stations.
    """

    def display(self, station: Station) -> str:
        """
        Display station in table row format.

        Args:
            station: Station to display

        Returns:
            str: Table row string
        """
        status = "✓" if station.has_data() else "✗"
        return f"| {station.name:20} | {status:^6} | {station.api_url:40} |"