"""Модуль calculator.

Содержит класс Calculator для выполнения основных арифметических операций.
"""


class Calculator:
    """Калькулятор для выполнения базовых арифметических операций."""

    def add(self, a: float, b: float) -> float:
        """Складывает два числа.

        Args:
            a: Первое слагаемое
            b: Второе слагаемое

        Returns:
            Сумма a и b
        """
        # TODO: реализовать сложение
        pass

    def subtract(self, a: float, b: float) -> float:
        """Вычитает одно число из другого.

        Args:
            a: Уменьшаемое
            b: Вычитаемое

        Returns:
            Разность a и b
        """
        # TODO: реализовать вычитание
        pass

    def multiply(self, a: float, b: float) -> float:
        """Умножает два числа.

        Args:
            a: Первый множитель
            b: Второй множитель

        Returns:
            Произведение a и b
        """
        # TODO: реализовать умножение
        pass

    def divide(self, a: float, b: float) -> float:
        """Делит одно число на другое.

        Args:
            a: Делимое
            b: Делитель

        Returns:
            Частное от деления a на b

        Raises:
            ZeroDivisionError: Если делитель равен нулю
        """
        # TODO: реализовать деление с проверкой делителя на ноль
        pass


def main() -> None:
    """Демонстрация работы калькулятора."""
    # TODO: создать экземпляр Calculator
    # TODO: протестировать все методы
    pass


if __name__ == "__main__":
    main()
