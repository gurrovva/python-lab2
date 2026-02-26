"""Модуль utils.

Содержит вспомогательные функции для валидации.
"""

from typing import Any


def validate_number(value: Any) -> bool:
    """Проверяет, является ли значение числом.

    Args:
        value: Проверяемое значение

    Returns:
        True если значение является числом, иначе False
    """
    # TODO: реализовать проверку значения на число
    # Подсказка: используйте isinstance(value, (int, float))
    pass


def validate_positive(value: float) -> bool:
    """Проверяет, является ли число положительным.

    Args:
        value: Проверяемое число

    Returns:
        True если число положительное, иначе False
    """
    # TODO: реализовать проверку на положительность
    pass


def main() -> None:
    """Демонстрация работы функций валидации."""
    # TODO: написать демонстрацию работы функций валидации
    pass


if __name__ == "__main__":
    main()
