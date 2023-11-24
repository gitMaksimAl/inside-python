from pathlib import Path
from random import randint

VOWELS = 'eyuioa'
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'
MIN_LENGTH = 4
MAX_LENGTH = 7


def pseudo_names(file_path: str | Path, count: int) -> None:
    vow_len = len(VOWELS)
    con_len = len(CONSONANTS)
    with open(file_path, 'a', encoding='utf-8') as f:
        for _ in range(count):
            f.write(CONSONANTS[(randint(0, con_len) + 31)
                               % con_len - 1].capitalize())
            for i in range(1, randint(MIN_LENGTH, MAX_LENGTH)):
                f.write(VOWELS[randint(0, vow_len - 1)])
                f.write(CONSONANTS[randint(0, con_len - 1)])
            f.write('\n')


if __name__ == '__main__':
    pseudo_names('names.txt', 5)
