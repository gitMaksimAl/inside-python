# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# имя файла без расширения или название каталога,
# расширение, если это файл,
# флаг каталога,
# название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

from collections import namedtuple
from pathlib import Path
import logging
import argparse

logging.basicConfig(level=logging.INFO,
                    filename='meta.log', encoding='utf-8')
loger1 = logging.getLogger(__name__)
File = namedtuple('File', 'name, extension, dir, parent')


def parse(loger: logging.getLogger, box: namedtuple):
    parser = argparse.ArgumentParser(prog='collect_meta()',
                                     description='Files metada collector.')
    parser.add_argument('-f', '--file_path', help='Directory',
                        required=True, type=Path)
    args = parser.parse_args()
    return collect_meta(args.file_path, box, loger)


def collect_meta(folder: Path, box: namedtuple, loger: logging.getLogger):
    for file in folder.iterdir():
        obj = box(file.stem if file.is_file() else file.name,
                  file.suffix, file.is_dir(), file.parent)
        loger.info(obj)
        if obj.dir:
            collect_meta(file, box, loger)


if __name__ == '__main__':
    parse(loger1, File)
