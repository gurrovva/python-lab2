from .utils import validate_number


class Calculator:
    def add(self, a: float, b: float) -> float:
        """Сложение двух чисел"""
        return validate_number(a) + validate_number(b)

    def subtract(self, a: float, b: float) -> float:
        """Вычитание двух чисел"""
        return validate_number(a) - validate_number(b)

    def multiply(self, a: float, b: float) -> float:
        """Умножение двух чисел"""
        return validate_number(a) * validate_number(b)

    def divide(self, a: float, b: float) -> float:
        """Деление двух чисел"""
        a = validate_number(a)
        b = validate_number(b)
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b
