from typing import Any


def validate() -> int | float:
    data = input('Please enter number: ')
    result = None
    try:
        result = float(data)
    except ValueError:
        try:
            result = int(data)
        except ValueError:
            print("Not a number")
    return result


def new_get(my_dict: dict, key: Any, default=None):
    try:
        return my_dict[key]
    except KeyError:
        return default
