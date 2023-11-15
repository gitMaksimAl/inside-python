# Создайте функцию-генератор.
# Функция генерирует N простых чисел,
# начиная с числа 2.
# Для проверки числа на простоту используйте правило: «число является простым,
# если делится нацело только на единицу и на себя».
from typing import Iterator


def is_prime(num: int) -> bool:
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def prime_generator(num: int) -> Iterator:
    prime_num = 2
    num -= 1
    yield prime_num
    while num:
        prime_num += 1
        if is_prime(prime_num):
            num -= 1
            yield prime_num


input_number = int(input('Please enter number: '))
for number in prime_generator(input_number):
    print(number)
