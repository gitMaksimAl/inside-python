"""
Folder walker with file meta collect.
"""
from pathlib import Path
import pickle
import csv
import json

__all__ = [
    'save_results_to_pickle',
    'save_results_to_json',
    'save_results_to_csv',
    'traverse_directory_list',
    'traverse_directory'
]


def __get_json(data: dict | list) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2)


def save_results_to_json(data: dict | list[dict], name: str) -> None:
    with open(name, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# TODO: how to unpack included dicts
def __get_csv(data: dict) -> None:
    pass


def save_results_to_csv(data: list[dict], name: str) -> None:
    headers = data[0].keys()
    with open(name, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers, dialect='excel-tab')
        writer.writeheader()
        writer.writerows(data)


def __get_pickle(data: dict) -> bytes:
    return pickle.dumps(data)


def save_results_to_pickle(data: list, name: str) -> None:
    with open(name, 'wb') as f:
        pickle.dump(data, f)


def get_dir_size(folder: dict) -> int:
    total_size = 0
    for item in folder.values():
        try:
            total_size += item['size']
        except TypeError:
            continue
    return total_size


def __get_dir_size__(folder: list, folder_name) -> int:
    total_size = 0
    for item_dict in folder:
        if item_dict['parent'] == folder_name:
            total_size += item_dict['size']
    return total_size


def __recursive_walker__(folder: Path, all: list) -> None:
    data = {}
    data['name'] = folder.name
    data['path'] = f"{folder.parent.resolve()}"
    data['parent'] = folder.parent.name
    data['size'] = folder.stat().st_size
    if folder.is_dir():
        for item in folder.iterdir():
            __recursive_walker__(item, all)
        data['type'] = 'folder'
        data['size'] = __get_dir_size__(all, folder.name)
    else:
        data['type'] = 'file'
    all.append(data)


def __recursive_walker(folder: Path) -> dict:
    data = {}
    data['path'] = f"{folder.parent.resolve()}"
    data['parent'] = folder.parent.name
    data['size'] = folder.stat().st_size
    if folder.is_dir():
        for item in folder.iterdir():
            data['type'] = 'folder'
            data[item.name] = __recursive_walker(item)
        # size all files
        data['size'] = get_dir_size(data)
        # data['size'] += get_dir_size()
    else:
        data['type'] = 'file'
    return data


def traverse_directory(directory: str | Path) -> str | None:
    save_method = {"json": save_results_to_json,
                   "csv": save_results_to_csv,
                   "pickle": save_results_to_pickle}
    if isinstance(directory, str):
        directory = Path(directory)
    if not directory.is_dir():
        raise ValueError
    return save_method["json"]({directory.name: __recursive_walker(directory)})


def traverse_directory_list(directory: str | Path) -> str | None:
    save_method = {"json": save_results_to_json,
                   "csv": save_results_to_csv,
                   "pickle": save_results_to_pickle}
    if isinstance(directory, str):
        directory = Path(directory)
    if not directory.is_dir():
        raise ValueError
    result = []
    __recursive_walker__(directory, result)
    return save_method["json"](result, directory.with_suffix('.json').name)

