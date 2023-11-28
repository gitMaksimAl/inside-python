from pathlib import Path
import json
import csv


def csv_to_json(source: str | Path) -> None:
    """

    :param source:
    :return:
    """
    csv_lines = []
    if isinstance(source, str):
        source = Path(source)
    target = Path.joinpath(source.parent / source.with_suffix('.json'))
    with (
        source.open('r', encoding='utf-8', newline='') as src,
        target.open('w', encoding='utf-8', newline='') as out
    ):
        reader = csv.reader(src, dialect='excel-tab')
        users = []
        for i, line in enumerate(reader):
            user = {}
            if i:
                level, user_id, user_name = line
                user['level'] = int(level)
                user['id'] = f"{int(user_id):010}"
                user['name'] = user_name.title()
                user['hash'] = hash(f"{user['name']}{user['id']}")
                users.append(user)
        json.dump(users, out, indent=2)


if __name__ == '__main__':
    csv_to_json('users.csv')
