from datetime import datetime


def get_days_from_today(date: str) -> int:
    try:
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
    except (ValueError, TypeError) as e:
        raise ValueError("Невірний формат дати. Очікується 'РРРР-ММ-ДД'.") from e

    today = datetime.today().date()
    return (today - target_date).days


if __name__ == "__main__":
    print(get_days_from_today("2020-10-09"))  # коректна дата
    print(get_days_from_today("2030-01-01"))  # майбутня дата -> від'ємне
    # print(get_days_from_today("bad-date"))  # має підняти ValueError