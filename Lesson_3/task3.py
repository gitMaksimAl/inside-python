# Создайте вручную кортеж содержащий элементы разных типов.
# Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

data = (42, 73, 3.14, 'Hello world', None, True, 'Text', 100500.2, False)
data_types = dict()

for item in data:
    item_type = type(item)
    key = data_types.setdefault(item_type, [])
    key.append(item)

print(data_types)
