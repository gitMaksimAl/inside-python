from pathlib import Path
import csv
import pickle


def pickle_to_csv(source: str | Path) -> None:
    if isinstance(source, str):
        source= Path(source)
    with (
            source.open('rb') as i,
            open(f"{source.parent}/{source.with_suffix('.csv').name}", 'w',
                 encoding='utf-8', newline='') as o
    ):
        data = pickle.load(i, encoding='utf-8')
        print(type(data))
        headers = list(data[0].keys())
        csv_writer = csv.DictWriter(o, fieldnames=headers, dialect='excel-tab',
                                    quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writeheader()
        csv_writer.writerows(data)


if __name__ == '__main__':
    pickle_to_csv('users.pickle')