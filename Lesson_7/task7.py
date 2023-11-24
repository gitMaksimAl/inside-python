# Создайте функцию для сортировки файлов по директориям: видео, изображения,
# текст и т.п. Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для
# сортировки.
from os import chdir
from pathlib import Path
from task5 import generate_files


def sort_files(path: Path, groups: dict[Path, list[str]]) -> None:
    if not path.is_dir():
        path.mkdir(parents=True)
    chdir(path)
    for file in path.iterdir():
        print(f'{file=}')
        for directory, ext in groups.items():
            if not directory.is_dir():
                directory.mkdir()
            if file.suffix[1:] in ext:
                file.replace(path / directory / file.name)


if __name__ == '__main__':
    # generate_files(Path.cwd(), txt=1, pdf=1, avi=1, mk4=1, png=1, gif=2)
    file_groups = {Path('video'): ['mp4', 'wav', 'avi', 'mk4'],
            Path('image'): ['png', 'jpg', 'jpeg', 'gif'],
            Path('doc'): ['docx', 'pdf', 'txt', 'doc']}
    sort_files(Path.cwd(), file_groups)
