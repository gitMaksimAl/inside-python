# Доработаем предыдущую задачу.
# Создайте новую функцию которая генерирует файлы с разными расширениями.
# Расширения и количество файлов функция принимает в качестве параметров.
# Количество переданных расширений может быть любым.
# Количество файлов для каждого расширения различно.
# Внутри используйте вызов функции из прошлой задачи.
from task4 import create_file
from pathlib import Path
from os import getcwd


def generate_files(file_path: str | Path, **kwargs) -> None:
    if isinstance(file_path, str):
        file_path = Path(file_path)
    if not file_path.is_dir():
        file_path.mkdir(parents=True)
    for ext in kwargs:
        create_file(ext, count=kwargs[ext])


if __name__ == '__main__':
    generate_files(file_path=getcwd(), txt=1, docx=1)
