"""Сохранение и загрузка депо транспорта в JSON и XML."""

import json
import os
import xml.etree.ElementTree as ET

from depot import Depot
from exceptions import RepositoryError
from models.factory import TransportFactory


class TransportRepository:
    """Репозиторий для Depot: JSON и XML."""

    # ---------- JSON ----------
    @staticmethod
    def save_json(depot: Depot, path: str) -> None:
        """Сохранить депо в JSON."""
        try:
            os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
            data = [v.to_dict() for v in depot.all()]
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except OSError as e:
            raise RepositoryError(f"Ошибка записи JSON: {e}") from e

    @staticmethod
    def load_json(path: str) -> Depot:
        """Загрузить депо из JSON."""
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            raise RepositoryError(f"Ошибка чтения JSON: {e}") from e

        depot = Depot()
        for item in data:
            depot.add(TransportFactory.from_dict(item))
        return depot

    # ---------- XML ----------
    @staticmethod
    def save_xml(depot: Depot, path: str) -> None:
        """Сохранить депо в XML."""
        try:
            os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
            root = ET.Element("depot")
            for v in depot.all():
                data = v.to_dict()
                veh_el = ET.SubElement(root, "vehicle", {"type": data["type"]})
                for key, value in data.items():
                    if key == "type":
                        continue
                    if isinstance(value, dict):
                        sub = ET.SubElement(veh_el, key)
                        for k, val in value.items():
                            ET.SubElement(sub, k).text = str(val)
                    elif value is None:
                        ET.SubElement(veh_el, key, {"nil": "true"})
                    else:
                        ET.SubElement(veh_el, key).text = str(value)

            tree = ET.ElementTree(root)
            ET.indent(tree, space="  ")
            tree.write(path, encoding="utf-8", xml_declaration=True)
        except OSError as e:
            raise RepositoryError(f"Ошибка записи XML: {e}") from e

    @staticmethod
    def load_xml(path: str) -> Depot:
        """Загрузить депо из XML."""
        try:
            tree = ET.parse(path)
        except (OSError, ET.ParseError) as e:
            raise RepositoryError(f"Ошибка чтения XML: {e}") from e

        root = tree.getroot()
        depot = Depot()

        for veh_el in root.findall("vehicle"):
            data: dict = {"type": veh_el.get("type")}
            for child in veh_el:
                if child.get("nil") == "true":
                    data[child.tag] = None
                elif len(child) > 0:
                    data[child.tag] = {sub.tag: sub.text for sub in child}
                else:
                    data[child.tag] = child.text
            depot.add(TransportFactory.from_dict(data))

        return depot