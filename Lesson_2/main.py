import sys
import typing
import math
import decimal

text = "Hello"
num = 10
fl_num = 1.3
names = ('Ivan', 'Artem', 'Gregori')
ls_nums = [1, 2, 3, 4]

BIN_BASE = 2
OCT_BASE = 8

CMD_DEPOSIT = 'd'
CMD_WITHDRAW = 'w'
CMD_EXIT = 'e'
MULTIPLICITY = 50
TAX = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_TAX = 30
MAX_TAX = 600
OPERATION_INTEREST = decimal.Decimal(3) / decimal.Decimal(100)
COUNT_FOR_INTEREST = 3
RICH_LIMIT = 5_000_000
RICH_TAX = decimal.Decimal(10) / decimal.Decimal(100)


def task1(obj):
    """
    Создайте несколько переменных разных типов.
    Проверьте к какому типу относятся созданные переменные.
    :param obj: 
    :return: 
    """
    return f"{obj=} - {type(object)}"


def task2(obj: typing.Iterable):
    """
    Создайте в переменной data список значений разных типов перечислив их через
    запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
    порядковый номер начиная с единицы
    значение
    адрес в памяти
    размер в памяти
    хэш объекта
    результат проверки на целое число только если он положительный
    результат проверки на строку только если он положительный.
    Добавьте в список повторяющиеся элементы и сравните на результаты.
    :param obj:
    :return: 
    """
    for index, item in enumerate(obj):
        print(f"{index} - {item=}, address - {id(item):#x},"
              f" size - {sys.getsizeof(item)},"
              f" hash - {hash(item)} - "
              f"{'string' if isinstance(item, str) else 'not string'}")


def task3(number: int) -> str:
    """
    Напишите программу, которая получает целое число и возвращает
    его двоичное, восьмеричное строковое представление.
    Функции bin и oct используйте для проверки своего
    результата, а не для решения.
    Дополнительно:
    Попробуйте избежать дублирования кода
    в преобразованиях к разным системам счисления
    Избегайте магических чисел
    Добавьте аннотацию типов где это возможно
    :param number:
    :return:
    """
    for base in BIN_BASE, OCT_BASE:
        prefix = '0b' if base == 2 else '0o'
        result = ''
        dividend = number

        while dividend > 0:
            remainder = dividend % base
            result = str(remainder) + result
            dividend //= base
        result = prefix + result

        print(f"{number=} in {base}`s base: {result}", end='\t')
        assert bin(number) == result if base == 2 else oct(number) == result
    print('')


def task4(diameter: str) -> None:
    """
    Напишите программу, которая вычисляет площадь
    круга и длину окружности по введённому диаметру.
    Диаметр не превышает 1000 у.е.
    Точность вычислений должна составлять
    не менее 42 знаков после запятой.
    :param diameter:
    :return:
    """
    d = decimal.Decimal(int(diameter))
    pi = decimal.Decimal(math.pi)
    area = pi * (d / 2) ** 2
    length = pi * d
    print(f"area - {area}, length - {length}")


def task5(a, b, c):
    """
    Напишите программу, которая решает квадратные уравнения даже если
    дискриминант отрицательный.
    Используйте комплексные числа
    для извлечения квадратного корня.
    :return: 
    """
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x = (-b + discriminant ** 0.5) / (2 * a)
        y = (-b - discriminant ** 0.5) / (2 * a)
        result = f"Equation has two roots: {x}, {y}"
    elif discriminant == 0:
        x = -b / (2 * a)
        result = f"Equation has one root: {x}"
    else:
        d = complex(discriminant)
        x = (-b + d ** 0.5) / (2 * a)
        y = (-b - d ** 0.5) / (2 * a)
        result = f"Equation has two roots: {x:g}, {y:g}"
    print(result)


def task6():
    """
    Напишите программу банкомат.
    Начальная сумма равна нулю
    Допустимые действия: пополнить, снять, выйти
    Сумма пополнения и снятия кратны 50 у.е.
    Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
    После каждой третей операции пополнения или снятия начисляются проценты - 3%
    Нельзя снять больше, чем на счёте
    При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
    операцией, даже ошибочной
    Любое действие выводит сумму денег.
    :return:
    """
    bank_account = 0
    operation_count = 0
    command = None
    print(f"Deposit: {CMD_DEPOSIT}, Withdraw: {CMD_WITHDRAW}, Exit: {CMD_EXIT}")
    while command != CMD_EXIT:
        command = input('Operation: ')
        if bank_account > RICH_LIMIT:
            bank_account -= bank_account * RICH_TAX

        operation_count += 1
        amount = 1
        while amount % MULTIPLICITY != 0:
            amount = int(input('Cant take less then 50RUB: '))
            if command == CMD_DEPOSIT:
                bank_account += amount
            elif command == CMD_WITHDRAW:
                percent = amount * TAX
                if percent < MIN_TAX:
                    percent = MIN_TAX
                elif percent > MAX_TAX:
                    percent = MAX_TAX
                if amount + percent <= bank_account:
                    bank_account -= percent + amount

            if operation_count % COUNT_FOR_INTEREST == 0:
                percent = bank_account * OPERATION_INTEREST
                bank_account += OPERATION_INTEREST
        print(f"Balance: {bank_account}")
        command = input('Operation: ')


print(task1(text))
print(task1(num))
print(task1(fl_num))
print(task1(names))
print(task1(ls_nums))

data = [42, 73.0, 'Hello world', True, 256, 2 ** 8, 'Hello world']
task2(data)

task3(int(input('Please enter positive number: ')))

task4(input('Please enter diameter of circle: '))

task5(int(input("a: ")), int(input("b: ")), int(input("c: ")))

task6()