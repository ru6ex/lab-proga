"""Собственные исключения предметной области пассажирского транспорта."""


class TransportError(Exception):
    """Базовое исключение для всех ошибок предметной области."""
    pass


class TransportNotFoundError(TransportError):
    """Транспортное средство не найдено в депо."""
    pass


class InvalidTransportDataError(TransportError):
    """Некорректные данные транспортного средства."""
    pass


class RepositoryError(TransportError):
    """Ошибка при работе с файлами (JSON/XML)."""
    pass