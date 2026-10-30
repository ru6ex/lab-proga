"""Класс Поезда Метро."""

from models.passenger_transport import PassengerTransport


class MetroTrain(PassengerTransport):
    """Поезд метро."""

    def __init__(
        self,
        line_color: str,
        cars_count: int,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.line_color = line_color
        self.cars_count = cars_count

    def get_info(self) -> str:
        return (
            f"Состав Метро {self.brand} {self.model} ({self.year} г.) | "
            f"Состав №: {self.vehicle_id} | Линия: {self.line_color} | Вагонов: {self.cars_count}"
        )

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({
            "line_color": self.line_color,
            "cars_count": self.cars_count,
        })
        return data