# Дан список повторяющихся элементов lst. Вернуть список с дублирующимися
# элементами. В результирующем списке не должно быть дубликатов.

lst = [1, 1, 2, 2, 3, 3, 4, -1, 7, 0, -1, 5]
items = {}
for i in lst:
    if not items.get(i):
        items[i] = 1
    else:
        items[i] += 1

duplicates = [i for i in items if items[i] > 1]
print(duplicates)
