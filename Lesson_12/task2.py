# TODO: Factorial must start begin from 0! and return from 'start'
class Generator:
    """
    Factorial calculate from 'start' and begin from 1! not from 0!.
    """

    def __init__(self, stop: int, *, start=1, step=1):
        self._start = start
        self._stop = stop
        self._step = step
        self._result = 1

    def __iter__(self):
        return self

    def __next__(self):
        while self._start < self._stop:
            for i in range(self._start, self._start + self._step):
                self._start += 1
                self._result *= i
            return self._result
        raise StopIteration


if __name__ == "__main__":
    factorial = Generator(12, step=3)
    for i in factorial:
        print(i)
