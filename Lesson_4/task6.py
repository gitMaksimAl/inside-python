# Функция получает на вход список чисел и два индекса.
# Вернуть сумму чисел между между переданными индексами.
# Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.

def slice_sum(data: list[int | float], index1: int, index2: int) -> int | float:
    start, end = min(index1, index2), max(index1, index2)
    start = start if start >= 0 else 0
    end = end if end < len(data) else len(data)
    return sum(data[start: end])


print(slice_sum([3, 4, 1, 10, 7, 13, 33, 91], 3, 5))
