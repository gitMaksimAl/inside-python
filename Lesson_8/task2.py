import json
from sys import stderr
from pathlib import Path


def get_data() -> tuple | None:
    name = input('Name: ')
    user_id = input('Id: ')
    level = input('Level: ')
    if name and user_id and level:
        return name, user_id, level
    return None


def prompt(file: str | Path):
    ids = set()
    if isinstance(file, str):
        file = Path(file)

    if file.is_file():
        with file.open('r', encoding='utf-8') as f:
            data = json.load(f)
            for _, user in data.items():
                # user id - key
                ids.update(user.keys())
    else:
        data = {str(lev): {} for lev in range(1, 8)}

    while d:=get_data():
        if d[1] in ids:
            print(f'User with id {d[1]} is exist!!!', file=stderr)
            continue
        ids.add(d[1])
        data[d[2]].update({d[1]: d[0]})
        with file.open('w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)


if __name__ == '__main__':
    prompt('users.json')
