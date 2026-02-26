def validate_number(value) -> float:
    """Проверяет, что значение является числом"""
    try:
        return float(value)
    except (TypeError, ValueError):
        raise ValueError(f"'{value}' не является числом")

def format_result(result: float, decimals: int = 2) -> str:
    """Форматирует результат с заданным количеством знаков"""
    return f"{result:.{decimals}f}"
