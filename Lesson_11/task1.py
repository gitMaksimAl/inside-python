# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)

import time


class MyStr(str):

    def __new__(cls, value: str, author: str):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time.time()
        return instance


# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При создании нового экземпляра класса, старые данные из ранее созданных
# экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра

class Archive:
    """
    Singleton class which store old values.
    """

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.archive_numbers = []
            cls.__instance.archive_text = []
        else:
            cls.__instance.archive_numbers.append(cls.__instance.num)
            cls.__instance.archive_text.append(cls.__instance.string)
        return cls.__instance

    def __init__(self, num: int, string: str):
        self.num = num
        self.string = string

    def __str__(self):
        return f"Number: {self.num}, string: {self.string}," \
               f" archive: {self.archive_text}, {self.archive_numbers}"


if __name__ == "__main__":
    text = MyStr("Python. Very nice", "Arkadi")
    print(f"{text=}, {text.author=}, {text.time=}\n")
    archive = Archive(1, 'First archive')
    archive2 = Archive(2, 'Second archive')
    archive3 = Archive(3, 'Third archive')

    print(f'{id(archive)=}, {id(archive2)=}, {id(archive3)=}\n'
          f'{archive3}')
