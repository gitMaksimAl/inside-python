"""
gb3474. Inside python. Seminar 1
"""
# task 1
REFORM = 1582
BIG_LEAP_YEAR = 400
SMALL_LEAP_YEAR = 4
LARGE_NON_LEAP_YEAR = 100
ZERO = 0

# task 2
MIN_NUM = 1
MAX_NUM = 999
FIRST_CONDITION = 10
SECOND_CONDITION = 100

# task3
CHARACTER = '*'
FILLER = ' '

# task4
LOWER_NUM = 2
UPPER_NUM = 10
COLUMNS = 4


def task1():
    """
    Напишите программу, которая запрашивает год и проверяет его на високосность.
    Распишите все возможные проверки в цепочке elif.
    Откажитесь от магических чисел
    Обязательно учтите год ввода Григорианского календаря
    В коде должны быть один input и один print
    :return:
    """
    result = None
    year = int(input('Please enter year: '))
    if REFORM > year:
        result = 'Year is not in Gregorian calendar.'
    elif year % BIG_LEAP_YEAR == ZERO:
        result = f'{year} - is leap year.'
    elif year % LARGE_NON_LEAP_YEAR == ZERO:
        result = f'{year} - not leap year'
    elif year % SMALL_LEAP_YEAR == ZERO:
        result = f'{year} - is leap year.'
    else:
        result = f'{year} - not leap year.'
    return result


def task2():
    """
    Пользователь вводит число от 1 до 999. Используя операции с числами
    сообщите что введено: цифра, двузначное число или трёхзначное число.
    Для цифры верните её квадрат, например 5 - 25
    Для двузначного числа произведение цифр, например 30 - 0
    Для трёхзначного числа его зеркальное отображение, например 520 - 25
    Если число не из диапазона, запросите новое число.
    Откажитесь от магических чисел
    В коде должны быть один input и один print
    :return:
    """
    result = 0
    remainder = 0
    num = MAX_NUM + 1
    while num < MIN_NUM or num > MAX_NUM:
        num = int(input('Please enter number: '))

    if num < FIRST_CONDITION:
        print(f'{num} - digit, power = {num * num}')
    elif num < SECOND_CONDITION:
        result = num // FIRST_CONDITION
        result *= num % FIRST_CONDITION
        print(f'{num} - two digit number, multiply = {result}')
    else:
        remainder = num
        while remainder > 10:
            result += remainder % FIRST_CONDITION
            result *= FIRST_CONDITION
            remainder //= FIRST_CONDITION
        result += remainder
        print(f'{num} - three digit number, mirror - {result}')


def task3():
    """
    Нарисовать в консоли ёлку спросив
    у пользователя количество рядов.
    Пример результата:
    Сколько рядов у ёлки?
    :return:
    """
    tree_levels = int(input('How many levels does the tree have? '))
    filler_len = tree_levels
    for line in range(tree_levels):
        for _ in range(filler_len):
            print(FILLER, end='')
        for _ in range(line):
            print(CHARACTER, end='')
        for _ in range(line + 1):
            print(CHARACTER, end='')
        print()
        filler_len -= 1


def task4():
    """
    Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
    :return:
    """
    for row_start in (LOWER_NUM, LOWER_NUM + COLUMNS):
        for j in range(LOWER_NUM, UPPER_NUM + 1):
            for i in range(row_start, row_start + COLUMNS):
                print(f"{i:>2} * {j:>2} = {i * j:>2}", end='\t')
            print()
        print()


task2()
task3()
task4()
