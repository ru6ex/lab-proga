"""Депо общественного транспорта: хранит ТС и реализует CRUD-операции."""

from exceptions import TransportNotFoundError
from models.passenger_transport import PassengerTransport


class Depot:
    """Контейнер транспортных средств депо."""

    def __init__(self) -> None:
        self._vehicles: list[PassengerTransport] = []

    # Создание
    def add(self, vehicle: PassengerTransport) -> None:
        """Добавить ТС в депо."""
        if self._find_by_id(vehicle.vehicle_id) is not None:
            raise ValueError(f"Транспорт с бортовым номером {vehicle.vehicle_id} уже существует")
        self._vehicles.append(vehicle)

    # Чтение
    def get_by_id(self, vehicle_id: str) -> PassengerTransport:
        """Найти ТС по бортовому номеру."""
        vehicle = self._find_by_id(vehicle_id)
        if vehicle is None:
            raise TransportNotFoundError(f"Транспорт с номером {vehicle_id} не найден")
        return vehicle

    def _find_by_id(self, vehicle_id: str) -> PassengerTransport | None:
        """Внутренний поиск без исключения."""
        for v in self._vehicles:
            if v.vehicle_id == vehicle_id:
                return v
        return None

    def all(self) -> list[PassengerTransport]:
        """Вернуть список всего транспорта."""
        return list(self._vehicles)

    def filter_by_brand(self, brand: str) -> list[PassengerTransport]:
        """Отфильтровать по марке."""
        return [v for v in self._vehicles if v.brand.lower() == brand.lower()]

    # Обновление
    def update(self, vehicle_id: str, **kwargs: object) -> PassengerTransport:
        """Обновить атрибуты ТС по бортовому номеру."""
        vehicle = self.get_by_id(vehicle_id)
        for key, value in kwargs.items():
            if not hasattr(vehicle, key):
                raise AttributeError(f"У транспорта нет атрибута {key}")
            setattr(vehicle, key, value)
        return vehicle

    # Удаление
    def delete(self, vehicle_id: str) -> None:
        """Удалить ТС по бортовому номеру."""
        vehicle = self.get_by_id(vehicle_id)
        self._vehicles.remove(vehicle)

    # Магические методы
    def __len__(self) -> int:
        return len(self._vehicles)

    def __iter__(self):
        return iter(self._vehicles)

    def __repr__(self) -> str:
        return f"Depot({len(self._vehicles)} vehicles)"