# Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# Строки нумеруются начиная с единицы.
# Задание №1 Слова выводятся отсортированными согласно кодировки Unicode.
# Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.

def put_sorted(text: str) -> None:
    sorted_text = sorted(text.split())
    max_len_word = len(max(sorted_text, key=len))
    for i, word in enumerate(sorted_text, 1):
        print(f"{i} {word:>{max_len_word}}")


put_sorted("Hello mister Anderson")
