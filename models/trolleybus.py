"""Класс Троллейбуса."""

from models.passenger_transport import PassengerTransport


class Trolleybus(PassengerTransport):
    """Троллейбус."""

    def __init__(
        self,
        battery_range_km: float,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.battery_range_km = battery_range_km  # Автономный ход

    def get_info(self) -> str:
        return (
            f"Троллейбус {self.brand} {self.model} ({self.year} г.) | "
            f"Борт №: {self.vehicle_id} | Автономный ход: {self.battery_range_km} км"
        )

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({
            "battery_range_km": self.battery_range_km,
        })
        return data