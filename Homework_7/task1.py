# Напишите функцию группового переименования файлов в папке test_folder под
# названием rename_files. Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании в
# конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно
# работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# f. Папка test_folder доступна из текущей директории
from pathlib import Path
from os import chdir


def rename_files(desired_name: str, num_digits: int,
                 source_ext: str, target_ext: str,
                 name_slice: list[int]=None) -> None:
    folder = 'test_folder'
    start = end = None
    if name_slice:
        start, end = name_slice
    if not target_ext.startswith('.'):
        target_ext = '.' + target_ext
    if Path(folder).is_dir():
        chdir(Path.cwd().joinpath(folder))
    for i, file in enumerate(Path.cwd().iterdir(), start=1):
        if file.suffix[1:] == source_ext:
            path = file.parent
            name = file.stem
            suff = file.suffix if not target_ext else target_ext
            file_name = f"{name[start: end]}{desired_name}{i:0={num_digits}}"
            print(file_name)
            file.replace(Path.joinpath(path, file_name).with_suffix(suff))


if __name__ == '__main__':
    rename_files(desired_name="", num_digits=3, source_ext="doc",
                 target_ext="png", name_slice=[0, 1])
