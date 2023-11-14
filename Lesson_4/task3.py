# Функция получает на вход строку из двух чисел через пробел.
# Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до
# наибольшего включительно.


def get_char_by_codes(text: str) -> dict[str, int]:
    num1, num2 = map(int, text.split())
    data = {chr(i): i for i in range(min(num1, num2), max(num1, num2) + 1)}
    return data


print(get_char_by_codes('243 345'))
