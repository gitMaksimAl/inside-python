from task1 import check_two_positional_args
from task2 import invoke_logg
from task3 import to_times


@check_two_positional_args
@to_times(3)
@invoke_logg
def guess_number(*args: int) -> str:
    """
    Guess number game.
    :param args: secret number and attempts count
    :return: str
    """
    num, count = args
    print(f"What number i guess?\nYou have {count} attempts!")
    result = "You lose"
    for i in range(1, count + 1):
        guess_number = int(input(f"Attempt {i}: "))
        if guess_number == num:
            result = "You win"
            break
        elif guess_number < num:
            print(f"{guess_number} less!")
        else:
            print(f"{guess_number} great!")
    print(result)
    return result


if __name__ == "__main__":
    # guess_number(100, 200)
    help(guess_number)
