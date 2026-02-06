from datetime import datetime


def get_days_from_today(date: str) -> int:
    """
    Завдання 1.

    Функція розраховує кількість днів між заданою датою і поточною датою.

    Параметри:
        date (str): дата у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').

    Повертає:
        int: кількість днів від заданої дати до поточної.
             Якщо задана дата пізніша за поточну — результат від'ємний.

    Примітки:
        - У розрахунках враховуються лише дні (час ігнорується).
        - Якщо формат дати неправильний — піднімається ValueError.
    """
    # Перевірка типу (на випадок, якщо передали не рядок)
    if not isinstance(date, str):
        raise TypeError("Параметр date має бути рядком у форматі 'РРРР-ММ-ДД'.")

    try:
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError as e:
        raise ValueError("Невірний формат дати. Очікується 'РРРР-ММ-ДД'.") from e

    today = datetime.today().date()
    return (today - target_date).days


if __name__ == "__main__":
    # Приклади / швидка самоперевірка

    # 1) Коректна дата в минулому
    print(get_days_from_today("2020-10-09"))

    # 2) Коректна дата в майбутньому (поверне від’ємне число)
    print(get_days_from_today("2030-01-01"))

    # 3) Некоректний формат — покажемо повідомлення, але не “впадемо” під час запуску файлу
    try:
        print(get_days_from_today("bad-date"))
    except ValueError as err:
        print(f"Помилка: {err}")