# Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.
DUPLICATES_COUNT = 2

data = [12, 2, 6, 43, 2, 11, 10, 7, 5, 12, 6, 17]
for item in set(data):
    if data.count(item) == DUPLICATES_COUNT:
        for _ in range(DUPLICATES_COUNT):
            data.remove(item)

print(data)
