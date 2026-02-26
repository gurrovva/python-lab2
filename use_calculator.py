from my_calculator import Calculator, format_result

# создаём экземпляр калькулятора
calc = Calculator()

# демонстрация всех операций
print("Арифметические операции:")
print(f"10 + 5 = {calc.add(10, 5)}")
print(f"10 - 5 = {calc.subtract(10, 5)}")
print(f"10 * 5 = {calc.multiply(10, 5)}")
print(f"10 / 5 = {calc.divide(10, 5)}")
print()

# демонстрация форматирования
print("Форматирование результатов:")
result = calc.divide(10, 3)
print(f"10 / 3 = {result} (без форматирования)")
print(f"10 / 3 = {format_result(result, 2)} (2 знака)")
print(f"10 / 3 = {format_result(result, 4)} (4 знака)")
print()

# демонстрация валидации
print("Валидация чисел:")
try:
    print(calc.add("10", 5))  # строка '10' преобразуется в число
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    print(calc.add("abc", 5))  # ошибка
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    print(calc.divide(10, 0))  # деление на ноль
except ValueError as e:
    print(f"Ошибка: {e}")