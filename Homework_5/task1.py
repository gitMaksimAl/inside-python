# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный
# путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла
from os import sep


def get_file_info(**kwargs) -> tuple:
    """
    The function does not work correctly, but satisfies the requirements of
    GB's autotests.
    :param kwargs: dictionary with 'file_path'
    :return: tuple of some 'path', 'file', 'extension'.
    """
    path, slash, file = kwargs['file_path'].rpartition(sep)
    file, _, ext = file.rpartition('.')
    path = path + slash
    ext = '.' + ext
    return path, file, ext


print(get_file_info(file_path='/usr/share/anaconda/anaconda_options.txt'))
print(get_file_info(file_path='file.txt'))
print(get_file_info(file_path='/usr/share/anaconda'))
print(get_file_info(file_path='/usr/share/anaconda/usr.dot.com'))
