import json
import pickle
from pathlib import Path


def json_to_pickle(source_folder: str | Path) -> None:
    if isinstance(source_folder, str):
        source_folder = Path(source_folder)
    if not source_folder.is_dir():
        raise ValueError
    for file in source_folder.iterdir():
        if file.suffix == '.json':
            with (
                file.open('r', encoding='utf-8') as f,
                open(f'{file.stem}.pickle', 'wb') as o
            ):
                data = json.load(f)
                pickle.dump(data, o)


if __name__ == '__main__':
    json_to_pickle(Path.cwd())
