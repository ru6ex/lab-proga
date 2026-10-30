"""Класс маршрута."""

from dataclasses import dataclass


@dataclass
class Route:
    route_number: str
    start_station: str
    end_station: str

    def to_dict(self) -> dict:
        return {
            "route_number": self.route_number,
            "start_station": self.start_station,
            "end_station": self.end_station,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Route":
        return cls(
            route_number=data["route_number"],
            start_station=data["start_station"],
            end_station=data["end_station"],
        )
    