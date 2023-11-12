from itertools import combinations
from pprint import pprint

items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0


# Соберите все возможные варианты рюкзаков из вещей весом не более допустимого
# duplicates present because cycle interrupted on weight
# can use set casting for delete duplicates
backpacks = []
sorted_items = sorted(items.items(), key=lambda it: it[1])
for i in range(1, len(sorted_items) + 1):
    for combination in combinations(sorted(items.items(),
                                           key=lambda it: it[1]), i):
        backpack = {}
        weight = 0
        for item in combination:
            if weight + item[1] > max_weight:
                break
            backpack[item[0]] = item[1]
            weight += item[1]
        backpacks.append(backpack)

pprint(backpacks)
