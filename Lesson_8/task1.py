# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.
import json
from pathlib import Path


def create_json_file(source: str | Path) -> None:
    if isinstance(source, str):
        source = Path(source)
    target = Path.joinpath(source.parent / source.with_suffix('.json'))
    dict_json = {}
    with (
        open(source.absolute(), 'r', encoding='utf-8') as src,
        open(target, 'w', encoding='utf-8') as out
    ):
        for line in src:
            name, number = line.rstrip('\n').split()
            dict_json[name.title()] = float(number)
        json.dump(dict_json, out, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    create_json_file('mix.txt')
