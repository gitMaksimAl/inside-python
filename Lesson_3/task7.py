# Пользователь вводит строку текста.
# Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# Результат сохраните в словаре, где ключ — символ, а значение — частота встречи
# символа в строке.
# Обратите внимание на порядок ключей. Объясните почему они совпадают
# или не совпадают в ваших решениях.

data = input('Please enter text: ')
data_characters = {}
for char in set(data):
    data_characters[char] = data.count(char)

data_characters2 = {}
for char in data:
    # get return 1 if True, if not set to 1
    data_characters2[char] = data_characters2.get(char, 0) + 1

# dict comprehension
# print({char: data.count(char) for char in set(data)})
print(data_characters)
print(data_characters2)
