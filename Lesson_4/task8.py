# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.


def replace_global_name_s() -> None:
    """
    WARNING: Function change global variables.
    :return: None
    """
    global_vars = [i for i in globals() if not i.startswith('__')]
    for key in global_vars:
        if key.endswith('s') and key != 's':
            globals()[key[:-1]] = globals()[key]
            globals()[key] = None


datas = [42, -73, 12, 85, -15, 2]
s = 'Hello world!'
names = ('NoName', 'OtherName', 'NewName')
sx = 42
print(globals())
replace_global_name_s()
print(globals())
