"""Базовый абстрактный класс пассажирского транспорта."""

from abc import ABC, abstractmethod
from models.driver import Driver
from models.route import Route


class PassengerTransport(ABC):
    """Абстрактное пассажирское транспортное средство."""

    def __init__(
        self,
        brand: str,
        model: str,
        year: int,
        capacity: int,
        vehicle_id: str,
        driver: Driver,
        route: Route | None = None,
    ) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.capacity = capacity
        self.vehicle_id = vehicle_id  # Бортовой/гос номер
        self.driver = driver
        self.route = route

    @abstractmethod
    def get_info(self) -> str:
        """Вернуть полную информацию о ТС."""
        pass

    def to_dict(self) -> dict:
        return {
            "type": self.__class__.__name__,
            "brand": self.brand,
            "model": self.model,
            "year": self.year,
            "capacity": self.capacity,
            "vehicle_id": self.vehicle_id,
            "driver": self.driver.to_dict(),
            "route": self.route.to_dict() if self.route else None,
        }