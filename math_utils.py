"""Модуль math_utils.

Содержит функции для работы с числами:
- Проверка на простоту
- Вычисление факториала
- Вычисление чисел Фибоначчи
"""


def is_prime(n: int) -> bool:
    """Проверяет, является ли число простым.

    Аргументы:
        n (int): Проверяемое число

    Возвращает:
        bool: True если число простое, False в противном случае
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def factorial(n: int) -> int:
    """Вычисляет факториал числа.

    Аргументы:
        n (int): Число для вычисления факториала

    Возвращает:
        int: Факториал числа n

    Исключения:
        ValueError: Если n отрицательное
    """
    if n < 0:
        raise ValueError("Факториал только для неотрицательных чисел")
    if n == 0:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n: int) -> int:
    """Возвращает n-е число Фибоначчи.

    Аргументы:
        n (int): Номер числа Фибоначчи (начиная с 0)

    Возвращает:
        int: n-е число Фибоначчи
    """
    if n < 0:
        raise ValueError("Число не может быть отрицательным")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def main() -> None:
    """Функция для демонстрации работы модуля."""
    print("Тестирование функций:")
    print(f"is_prime(7) = {is_prime(7)}")
    print(f"factorial(5) = {factorial(5)}")
    print(f"fibonacci(7) = {fibonacci(7)}")


if __name__ == "__main__":
    main()