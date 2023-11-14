# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

def get_sorted_chars(text: str) -> list[int]:
    codes = set()
    for char in set(text):
        codes.add(ord(char))
    return sorted(codes, reverse=True)


print(get_sorted_chars("Hello mister Anderson"))
