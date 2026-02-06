import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """
    Завдання 2.

    Генерує набір унікальних випадкових чисел для лотереї.

    Параметри:
        min (int): мінімальне число у наборі (не менше 1).
        max (int): максимальне число у наборі (не більше 1000).
        quantity (int): кількість чисел, які потрібно вибрати.

    Повертає:
        list[int]: відсортований список унікальних чисел.
                   Якщо параметри некоректні — повертає порожній список [].
    """
    # Перевірка типів (щоб "впоратися" з некоректним вводом)
    if not all(isinstance(x, int) for x in (min, max, quantity)):
        return []

    # Перевірка обмежень за умовою
    if min < 1 or max > 1000:
        return []

    # Мінімум має бути менше максимуму
    if min > max:
        return []

    # Кількість має бути в межах діапазону і не перевищувати кількість доступних чисел
    available_count = max - min + 1
    if quantity < 1 or quantity > available_count:
        return []

    # Генеруємо унікальні числа (sample гарантує унікальність)
    numbers = random.sample(range(min, max + 1), quantity)

    # Повертаємо відсортований список
    return sorted(numbers)


if __name__ == "__main__":
    print("✅ Валідний приклад:", get_numbers_ticket(1, 49, 6))

    tests = [
        (0, 49, 6),
        (1, 2000, 6),
        (10, 5, 2),
        (1, 5, 10),
    ]

    for t in tests:
        print(f"❌ Невалідні параметри {t} -> {get_numbers_ticket(*t)}")