"""
Folder walker with file meta collect.
"""
from typing import Any
from pathlib import Path
import pickle
import csv
import json

__all__ = [
    'save_results_to_pickle',
    'save_results_to_json',
    'save_results_to_csv',
    'traverse_directory'
]


def __no_format(data: dict | list) -> dict | list:
    """
    Represent data as is
    :param data:
    :return:
    """
    return data


def __get_json(data: dict | list) -> str:
    """
    Represent data like JSON string
    :param data:
    :return:
    """
    return json.dumps(data, ensure_ascii=False, indent=2)


def save_results_to_json(data: dict | list[dict], name: str) -> None:
    """
    Save data to JSON file
    :param data:
    :param name: file name with suffix
    :return:
    """
    with open(name, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def __get_csv(data: dict) -> list[dict[str, Any]]:
    """
    Flatten representation of the folder. Can use by save_result_to_csv func
    :param data: dictionary
    :return: list of the dictionaries
    """
    unpacked = []
    item = {}
    for k, v in data.items():
        if isinstance(v, dict):
            unpacked.extend(__get_csv(data[k]))
        else:
            item[k] = v
    if item:
        unpacked.append(item)
    return unpacked


def save_results_to_csv(data: list[dict], name: str) -> None:
    """
    Save data to csv file with default dialect
    :param data:
    :param name: file name with suffix
    :return:
    """
    headers = data[0].keys()
    with open(name, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers, dialect='excel-tab')
        writer.writeheader()
        writer.writerows(data)


def __get_pickle(data: dict | list) -> bytes:
    """
    Represent data like bytes string
    :param data:
    :return:
    """
    return pickle.dumps(data)


def save_results_to_pickle(data: list, name: str) -> None:
    """
    Save data to PICKLE file
    :param data:
    :param name: file name with suffix
    :return:
    """
    with open(name, 'wb') as f:
        pickle.dump(data, f)


def get_dir_size(folder: dict) -> int:
    """
    Collect size of the included file
    :param folder:
    :return: summary size of the files
    """
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


def __recursive_walker(folder: Path) -> dict:
    """
    Recursive folders walker
    :param folder: folder like Path object
    :return: dict of dicts
    """
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
    else:
        data['type'] = 'file'
    return data


def traverse_directory(directory: str | Path,
                       *, data_format="no") -> str | None:
    """
    Walker of the folder and collect meta
    :param directory: str -> Path
    :param data_format: default - no formatted. Can be any of
    "json, csv, pickle"
    :return: dict of dicts by default or str or list of dicts or bytes
    """
    if isinstance(directory, str):
        directory = Path(directory)
    if not directory.is_dir():
        raise ValueError
    data = {directory.name: __recursive_walker(directory)}
    return _FORMATTED[data_format](data)


_TO_FILE = {
    "json": save_results_to_json,
    "csv": save_results_to_csv,
    "pickle": save_results_to_pickle
}

_FORMATTED = {
    "json": __get_json,
    "csv": __get_csv,
    "pickle": __get_pickle,
    "no": __no_format
}
