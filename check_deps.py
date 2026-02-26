"""Скрипт для проверки установленных зависимостей.

Позволяет проверить, какие пакеты установлены в текущем окружении.
"""


def check_package_installed(package_name: str) -> bool:
    """Проверяет, установлен ли пакет.

    Args:
        package_name: Имя пакета для проверки

    Returns:
        True если пакет установлен, иначе False
    """
    # TODO: получить список установленных пакетов через pkg_resources или subprocess
    # Подсказка: можно использовать importlib.metadata или pkg_resources
    pass


def get_package_version(package_name: str) -> str | None:
    """Возвращает версию установленного пакета.

    Args:
        package_name: Имя пакета

    Returns:
        Версия пакета или None, если пакет не установлен
    """
    # TODO: получить версию пакета
    pass


def check_dependencies() -> None:
    """Проверяет наличие требуемых зависимостей."""
    # Список пакетов для проверки
    required_packages = [
        "requests",
        "click",
        "pydantic",
    ]

    # TODO: проверить наличие требуемых пакетов
    # Подсказка: используйте функции check_package_installed и get_package_version

    # TODO: вывести список версий установленных пакетов
    pass


def main() -> None:
    """Точка входа для проверки зависимостей."""
    check_dependencies()


if __name__ == "__main__":
    main()
