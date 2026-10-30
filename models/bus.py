"""Класс Автобуса."""

from models.passenger_transport import PassengerTransport


class Bus(PassengerTransport):
    """Автобус."""

    def __init__(
        self,
        fuel_type: str,
        is_articulated: bool,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.fuel_type = fuel_type
        self.is_articulated = is_articulated  # Автобус с гармошкой или нет

    def get_info(self) -> str:
        articulated_str = "с гармошкой" if self.is_articulated else "обычный"
        return (
            f"Автобус {self.brand} {self.model} ({self.year} г.) | "
            f"Борт №: {self.vehicle_id} | Мест: {self.capacity} | "
            f"Топливо: {self.fuel_type} ({articulated_str})"
        )

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({
            "fuel_type": self.fuel_type,
            "is_articulated": self.is_articulated,
        })
        return data
    