import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    if not all(isinstance(x, int) for x in (min, max, quantity)):
        return []

    if min < 1 or max > 1000 or min > max:
        return []

    if quantity < 1 or quantity > (max - min + 1):
        return []

    return sorted(random.sample(range(min, max + 1), quantity))


if __name__ == "__main__":
    print(get_numbers_ticket(1, 49, 6))   # валідний приклад
    print(get_numbers_ticket(1, 5, 10))   # невалідний -> []