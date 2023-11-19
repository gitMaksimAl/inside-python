from sys import argv
from task1 import guess_number


if __name__ == '__main__':
    script, *param = argv
    print(f"{'Win' if guess_number(*(int(n) for n in param)) else 'Lose'}")
