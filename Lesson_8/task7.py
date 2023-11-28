from pathlib import Path
import csv


def csv_to_pickles(source: str | Path) -> list[dict]:
    if isinstance(source, str):
        source= Path(source)
    pickle_data = []
    with source.open('r', encoding='utf-8', newline='') as src:
        data = csv.reader(src, dialect='excel-tab')
        for i, line in enumerate(data):
            if not i:
                headers = line
            else:
                pickle_data.append(dict(zip(headers, line)))
    return pickle_data


if __name__ == "__main__":
    print(csv_to_pickles("users.csv"))
