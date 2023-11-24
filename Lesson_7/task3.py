# Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# если результат умножения отрицательный, сохраните имя записанное строчными
# буквами и произведение по модулю
# если результат умножения положительный, сохраните имя прописными буквами и
# произведение округлённое до целого.
# В результирующем файле должно быть столько же строк, сколько в более
# длинном файле.
# При достижении конца более короткого файла,
# возвращайтесь в его начало.
from os import stat, getcwd, sep
from pathlib import Path
from typing import TextIO


def text_looping(io: TextIO) -> str:
    text = io.readline()
    if not text:
        io.seek(0)
        text = io.readline()
    return text[:-1]


def mix_files(source_file1: str | Path,
              source_file2: str | Path,
              out_file: str | Path) -> None:
    with (
        open(source_file1, 'r', encoding='utf-8') as numbers,
        open(source_file2, 'r', encoding='utf-8') as names,
        open(out_file, 'w', encoding='utf-8') as output
    ):
                numbers_len = sum((1 for i in numbers))
                names_len = sum((1 for i in names))
                numbers.seek(0)
                names.seek(0)
                for i in range(numbers_len if numbers_len > names_len
                               else names_len):
                    print(i)
                    name = text_looping(names)
                    num1, num2 = text_looping(numbers).split(' | ')
                    mult = int(num1) * float(num2)
                    if mult < 0:
                        output.write(f'{name.lower()} {-mult}\n')
                    elif mult > 0:
                        output.write(f'{name.upper()} {int(mult)}\n')


if __name__ == '__main__':
    mix_files('numbers.txt', 'names.txt', 'mix.txt')
