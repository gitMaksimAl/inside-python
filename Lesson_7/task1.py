# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.
import random
from pathlib import Path


MIN_VALUE = -1_000
MAX_VALUE = 1_000


def fill_file(name: str | Path, rows: int) -> None:
    with open(name, 'a', encoding='utf-8') as f:
        for _ in range(rows):
            int_value = random.randint(MIN_VALUE, MAX_VALUE)
            float_value = random.uniform(MIN_VALUE, MAX_VALUE)
            f.write(f'{int_value} | {float_value}\n')


if __name__ == '__main__':
    fill_file('numbers.txt', 50)
