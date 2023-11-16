# Создайте функцию генератор чисел Фибоначчи fibonacci.
from typing import Generator


def fibonacci() -> Generator:
    """
    Fibonacci number generator.
    :return:
    """
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, b + a


f = fibonacci()
for i in range(10):
    print(next(f))
