import argparse
from datetime import datetime
from timeit import Timer
import logging
from functools import partial

from src.ChessyPackage.queen_generator import QueensGenerator


def parse():
    parser = argparse.ArgumentParser(prog="main.py", description="Generate n "
                                     "boards with m queens")
    parser.add_argument("--queens", default=8, help="count of queens on "
                                                    "the board", type=int)
    parser.add_argument("--x_start", default=1, help="can start from 1 or ascii"
                                                     " char(NOT IMPLEMENTED)",
                        type=int)
    parser.add_argument("--y_start", default=1, help="can start from 1 or ascii"
                                                     " char(NOT IMPLEMENTED)",
                        type=int)
    parser.add_argument("--boards", default=4, help="output file", type=int)
    parser.add_argument("--repeat", default=1, help="count of generations",
                        type=int)
    parser.add_argument("--file", default="q_gen.log", help="output file")
    args = parser.parse_args()
    return start(QueensGenerator(args.queens, args.x_start, args.y_start),
                 args.boards, args.repeat, args.file)


def start(gen, boards, repeats, file):
    logging.basicConfig(filename=file, filemode='a', level=logging.INFO,
                        encoding='utf-8')
    loger = logging.getLogger(__name__)
    timer = Timer(partial(gen.generate_boards, boards))
    loger.info(f"{datetime.now()} args: {boards} boards, "
               f"{repeats} times - {timer.timeit(repeats)}")


if __name__ == "__main__":
    parse()
