from datetime import datetime

def get_days_from_today(date_str: str) -> int:
    """
    Calculates the number of days between the given date (YYYY-MM-DD) and today.
    Returns a negative number if the given date is in the future.
    Ignores time (hours/minutes/seconds).
    """
    try:
        target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return 0

    today = datetime.today().date()
    return (today - target_date).days


if __name__ == "__main__":
    # Quick self-checks
    print(get_days_from_today("2020-10-09"))
    print(get_days_from_today("2030-01-01"))
    print(get_days_from_today("bad-date"))