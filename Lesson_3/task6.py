# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# Строки нумеруются начиная с единицы.
# Слова выводятся отсортированными согласно кодировки Unicode.
# Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

input_data = input('Please enter a text: ').split()
input_data.sort()
format_width = 0
for word in input_data:
    length = len(word)
    if length > format_width:
        format_width = length

for i, word in enumerate(input_data, 1):
    print(f"{i}. {word:>{format_width}}")
