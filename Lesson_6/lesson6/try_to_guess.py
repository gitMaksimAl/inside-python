# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и
# количество попыток. Внутри генерируется случайное число в указанных границах и
# пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

from random import randint

__all__ = ['guess_number']


def guess_number(less: int = 0, larger: int = 10, attempt: int = 5) -> bool:
    num = randint(less, larger)
    while (guess := int(input('What number did I guess: '))) != num and \
            attempt != 0:
        print(f"I guess number {'>' if num > guess else '<'} {guess}")
        attempt -= 1
    print(num)
    return True if guess == num else False


if __name__ == '__main__':
    print(f"{'Win' if guess_number() else 'Lose'}")
