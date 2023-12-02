# Task1
# Создайте функцию-замыкание, которая запрашивает два целых числа:
# от 1 до 100 для загадывания,
# от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит угадать загаданное
# число за указанное число попыток

from random import randint
from typing import Callable
from functools import wraps


def foo() -> Callable[[], None]:
    num = randint(1, 100)
    count = randint(1, 10)

    def bar():
        print(f"What number i guess?\nYou have {count} attempts!")
        result = "Lose"
        for i in range(1, count + 1):
            guess_number = int(input(f"Attempt {i}: "))
            if guess_number == num:
                result = "Win"
                break
            elif guess_number < num:
                print(f"{guess_number} less!")
            else:
                print(f"{guess_number} great!")
        print(result)

    return bar


# Task2
# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию-угадайку числа в
# диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов.

BOTTOM_NUM = 1
TOP_NUM = 100
BOTTOM_ATTEMPT = 1
TOP_ATTEMPT = 10


# two positional argument wrapper
def check_two_positional_args(func: Callable) -> Callable:

    @wraps(func)
    def wrapp(*args: int) -> None:
        num, count = args
        if not (BOTTOM_NUM < num < TOP_NUM):
            num = randint(BOTTOM_NUM, TOP_NUM)
        if not (BOTTOM_ATTEMPT < count < TOP_ATTEMPT):
            count = randint(BOTTOM_ATTEMPT, TOP_ATTEMPT)
        return func(num, count)

    return wrapp


@check_two_positional_args
def bar(*args: int) -> str:
    num, count = args
    print(f"What number i guess?\nYou have {count} attempts!")
    result = "You lose"
    for i in range(1, count + 1):
        guess_number = int(input(f"Attempt {i}: "))
        if guess_number == num:
            result = "You win"
            break
        elif guess_number < num:
            print(f"{guess_number} less!")
        else:
            print(f"{guess_number} great!")
    return result


if __name__ == "__main__":
    bar(200, 2000)
