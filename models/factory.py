"""Фабрика для восстановления объектов из словаря."""

from exceptions import InvalidTransportDataError
from models.bus import Bus
from models.driver import Driver
from models.metro_train import MetroTrain
from models.passenger_transport import PassengerTransport
from models.route import Route
from models.tram import Tram
from models.trolleybus import Trolleybus


class TransportFactory:
    """Фабрика создания транспорта из словаря."""

    @staticmethod
    def from_dict(data: dict) -> PassengerTransport:
        tp_type = data.get("type")
        
        # Разбираем вложенные объекты
        driver_data = data.get("driver")
        driver = Driver.from_dict(driver_data) if isinstance(driver_data, dict) else None
        
        route_data = data.get("route")
        route = Route.from_dict(route_data) if isinstance(route_data, dict) else None

        base_kwargs = {
            "brand": data.get("brand"),
            "model": data.get("model"),
            "year": int(data.get("year", 0)),
            "capacity": int(data.get("capacity", 0)),
            "vehicle_id": data.get("vehicle_id"),
            "driver": driver,
            "route": route,
        }

        if tp_type == "Bus":
            return Bus(
                fuel_type=data.get("fuel_type"),
                is_articulated=str(data.get("is_articulated")).lower() == "true",
                **base_kwargs,
            )
        elif tp_type == "Tram":
            return Tram(
                carriages_count=int(data.get("carriages_count", 1)),
                track_width=float(data.get("track_width", 1.524)),
                **base_kwargs,
            )
        elif tp_type == "Trolleybus":
            return Trolleybus(
                battery_range_km=float(data.get("battery_range_km", 0.0)),
                **base_kwargs,
            )
        elif tp_type == "MetroTrain":
            return MetroTrain(
                line_color=data.get("line_color"),
                cars_count=int(data.get("cars_count", 4)),
                **base_kwargs,
            )
        else:
            raise InvalidTransportDataError(f"Неизвестный тип транспорта: {tp_type}")