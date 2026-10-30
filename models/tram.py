"""Класс Трамвая."""

from models.passenger_transport import PassengerTransport


class Tram(PassengerTransport):
    """Трамвай."""

    def __init__(
        self,
        carriages_count: int,
        track_width: float,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.carriages_count = carriages_count
        self.track_width = track_width

    def get_info(self) -> str:
        return (
            f"Трамвай {self.brand} {self.model} ({self.year} г.) | "
            f"Борт №: {self.vehicle_id} | Вагонов: {self.carriages_count} | "
            f"Ширина колеи: {self.track_width} м"
        )

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({
            "carriages_count": self.carriages_count,
            "track_width": self.track_width,
        })
        return data