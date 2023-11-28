import csv
import json
from pathlib import Path


def json_to_csv(source: str | Path) -> None:
    if isinstance(source, str):
        source = Path(source)
    target = Path.joinpath(source.parent / source.with_suffix('.csv'))
    lines = []
    with source.open('r', encoding='utf-8') as f:
        data = json.load(f)
    for level, user in data.items():
        for id, name in user.items():
            lines.append({'level': int(level), 'id': int(id), 'name': name})
    with target.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f,
                                fieldnames=['level', 'id', 'name'],
                                dialect='excel-tab')
        writer.writeheader()
        writer.writerows(lines)


if __name__ == '__main__':
    json_to_csv('users.json')
