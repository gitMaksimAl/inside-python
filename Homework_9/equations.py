import csv
from sys import stderr
from typing import Callable
from csv import writer
from json import dump
from functools import wraps
from pathlib import Path
from random import randint

__LEAST_NUMBER_OF_ARGUMENTS = 100
__GREATEST_NUMBER_OF_ARGUMENTS = 1000
__IN_FILE = 'input_data.csv'
__OUT_FILE = 'results.json'


def generator_limit(func: Callable) -> Callable:
    """
    Decorator for limit 2d positional argument
    :param func: function with two positional args
    :return: wrapper func
    """

    def wrapper(*args) -> None:
        file_name, rows = args
        if rows < __LEAST_NUMBER_OF_ARGUMENTS:
            rows = __LEAST_NUMBER_OF_ARGUMENTS
        elif rows > __GREATEST_NUMBER_OF_ARGUMENTS:
            rows = __GREATEST_NUMBER_OF_ARGUMENTS

        func(file_name, rows)

    return wrapper


@generator_limit
def generate_csv_file(file_name: str, rows: int) -> None:
    """
    KSV file generator with n-strings of a set of numbers of 3
    :param file_name: file name with csv extension
    :param rows: number of sets of number
    :return: no return. Artefact - file
    """
    args_list = []
    for _ in range(rows):
        args_list.append((randint(-20, 20),
                          randint(1, 77),
                          randint(-3, 33)))
    file_name = Path(file_name)
    headers = ['a', 'b', 'c']
    with file_name.open('w', encoding='utf-8', newline='') as f:
        csv_writer = writer(f,
                            dialect='excel-tab',
                            quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writerow(headers)
        csv_writer.writerows(args_list)


def save_to_json(file: str) -> Callable:
    """
    Decorator for save func result to json file.
    :param file: file name
    :return: artefact JSON file
    """

    def func_call(func: Callable) -> Callable:

        @wraps(func)
        def wrapp() -> None:
            in_data = []
            with open(file, 'r', encoding='utf-8', newline='') as i:
                reader = csv.DictReader(i, fieldnames=['a', 'b', 'c'],
                                        dialect='excel-tab',
                                        quoting=csv.QUOTE_NONNUMERIC)
                for num_set in reader:
                    in_data.append(num_set)
            in_data.remove(in_data[0])
            for equation in in_data:
                equation['result'] = func(**equation)
            with open(__OUT_FILE, 'w', encoding='utf-8', newline='') as o:
                dump(in_data, o, indent=2)

        return wrapp

    return func_call


@save_to_json(__IN_FILE)
def find_roots(a: int, b: int, c: int) -> tuple[float, float] | float | None:
    """
    Find roots of the quadratic equations.
    :param a:
    :param b:
    :param c:
    :return:
    """
    x = y = None
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        try:
            x = (-b + discriminant ** 0.5) / (2 * a)
            y = (-b - discriminant ** 0.5) / (2 * a)
        except ZeroDivisionError:
            print(f"{a=}, {b=}, {c=}: Division by Zero!!", file=stderr)
        return x, y
    elif discriminant == 0:
        return -b / (2 * a)
    return None


if __name__ == "__main__":
    generate_csv_file(__IN_FILE, 55)
    find_roots()
