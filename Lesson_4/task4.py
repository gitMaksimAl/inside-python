# Функция получает на вход список чисел.
# Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# Как вариант напишите сортировку пузырьком.

def bubble_sort(data: list[int]) -> list[int]:
    length = len(data) - 1
    while length > 0:
        for i in range(length):
            if data[i] > data[i + 1]:
                data[i + 1], data[i] = data[i], data[i + 1]
        length -= 1
    return data


print(bubble_sort([9, 1, 6, 8, 4, 7, 2, 0, 3, 5]))
