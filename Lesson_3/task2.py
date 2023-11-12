# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# Целое положительное число
# Вещественное положительное или отрицательное число
# Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# Строку в верхнем регистре в остальных случаях

input_text = input('Please enter something: ')
items = input_text.split(' ')
for item in items:
    if item.count('.') == 1:
        try:
            print(f"float: {float(item)}")
        except ValueError:
            pass
    elif item.isdigit() or (item[0] == '-' and item[1:].isdigit()):
        print(f"int: {int(item)}")
    elif not item.islower():
        print(f"string: {item.lower()}")
    else:
        print(f"string: {item.upper()}")
