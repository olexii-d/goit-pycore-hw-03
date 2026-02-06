from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    today = datetime.today().date()
    end_date = today + timedelta(days=7)

    result = []

    for user in users:
        name = user.get("name")
        bday_str = user.get("birthday")

        if not name or not bday_str:
            continue

        try:
            birthday = datetime.strptime(bday_str, "%Y.%m.%d").date()
        except ValueError:
            continue

        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if today <= birthday_this_year <= end_date:
            congratulation_date = birthday_this_year

            # 5 = Saturday, 6 = Sunday
            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            result.append({
                "name": name,
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return result


if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.02.17"},
        {"name": "Jane Smith", "birthday": "1990.02.10"},
    ]

    print(get_upcoming_birthdays(users))