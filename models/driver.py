"""Класс водителя/машиниста."""

from dataclasses import dataclass


@dataclass
class Driver:
    name: str
    license_category: str

    def to_dict(self) -> dict:
        return {"name": self.name, "license_category": self.license_category}

    @classmethod
    def from_dict(cls, data: dict) -> "Driver":
        return cls(name=data["name"], license_category=data["license_category"])