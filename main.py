"""Демонстрация работы с депо пассажирского транспорта."""

from depot import Depot
from exceptions import TransportError, TransportNotFoundError
from models.bus import Bus
from models.driver import Driver
from models.metro_train import MetroTrain
from models.route import Route
from models.tram import Tram
from models.trolleybus import Trolleybus
from repository import TransportRepository


def build_demo_depot() -> Depot:
    """Создать демонстрационное депо."""
    depot = Depot()

    depot.add(Bus(
        brand="ЛИАЗ", model="5292", year=2021, capacity=108,
        vehicle_id="BUS-001", fuel_type="КПГ (Газ)", is_articulated=False,
        driver=Driver("Иванов И.И.", "D"),
        route=Route("m1", "Северный терминал", "Южный терминал"),
    ))
    depot.add(Tram(
        brand="Витязь-М", model="71-931M", year=2022, capacity=180,
        vehicle_id="TRAM-102", carriages_count=3, track_width=1.524,
        driver=Driver("Петрова А.С.", "Tm"),
        route=Route("17", "Останкино", "Медведково"),
    ))
    depot.add(Trolleybus(
        brand="ПК ТС", model="6281 Адмирал", year=2023, capacity=96,
        vehicle_id="TRL-304", battery_range_km=20.0,
        driver=Driver("Сидоров В.В.", "Tb"),
    ))
    depot.add(MetroTrain(
        brand="Метровагонмаш", model="81-775 Москва-2020", year=2024, capacity=1400,
        vehicle_id="METRO-77", line_color="Красная", cars_count=8,
        driver=Driver("Смирнов К.А.", "Metro"),
    ))

    return depot


def main() -> None:
    try:
        depot = build_demo_depot()
        print(f"Создано депо: {depot}")
        print("-" * 60)
        for v in depot.all():
            print(v.get_info())

        # Обновление
        print("\n UPDATE: смена водителя трамвая")
        depot.update("TRAM-102", driver=Driver("Кузнецов Н.Н.", "Tm"))
        print(f"Новый водитель: {depot.get_by_id('TRAM-102').driver.name}")

        # Чтение
        print("\n READ: поиск по марке ЛИАЗ")
        for v in depot.filter_by_brand("ЛИАЗ"):
            print(v.get_info())

        # Исключение 
        print("\n Обработка ошибки")
        try:
            depot.get_by_id("BUS-999")
        except TransportNotFoundError as e:
            print(f"Поймано исключение: {e}")

        # JSON
        TransportRepository.save_json(depot, "data/depot.json")
        depot_from_json = TransportRepository.load_json("data/depot.json")
        print(f"\nЗагружено из JSON: {depot_from_json}")

        # XML
        TransportRepository.save_xml(depot, "data/depot.xml")
        depot_from_xml = TransportRepository.load_xml("data/depot.xml")
        print(f"Загружено из XML: {depot_from_xml}")

        # DELETE
        depot.delete("TRL-304")
        print(f"\nПосле удаления: {depot}")

    except TransportError as e:
        print(f"Ошибка предметной области: {e}")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()