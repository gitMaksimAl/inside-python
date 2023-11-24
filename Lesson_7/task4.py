# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.
from random import randint, choices
from string import ascii_lowercase


def create_file(extension: str, min_name: int=6, max_name: int=30,
                min_size: int=256, max_size: int=4096, count: int=42) -> None:
    for _ in range(count):
        name = ''.join(choices(ascii_lowercase, k=randint(min_name, max_name)))
        file = f"{name}.{extension}"
        data = bytes(randint(0, 255)
                    for _ in range(randint(min_size, max_size)))
        with open(file, 'wb') as f:
            f.write(data)


if __name__ == '__main__':
    create_file('txt', 8, 15, count=4)
