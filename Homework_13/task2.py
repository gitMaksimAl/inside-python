class InvalidTextError(ValueError):

    def __init__(self, text: str):
        super().__init__(f"Invalid text: {text}."
                         f" Text should be a non-empty string.")


class InvalidNumberError(ValueError):

    def __init__(self, number: int | float):
        super().__init__(f"Invalid number: {number}."
                         f" Number should be a positive integer or float")


class TrueValue:

    def __set_name__(self, owner, name):
        self.__name = f"_{name}"

    def __set__(self, instance, value: str | float | int):
        if isinstance(value, (int, float)) and value <= 0:
            raise InvalidNumberError(value)
        elif isinstance(value, str) and value == "":
            raise InvalidTextError(value)
        setattr(instance, self.__name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.__name)


class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    text = TrueValue()
    number = TrueValue()
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: int | float):
        self.text = text
        self.number = number

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. ' \
               f'Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'


if __name__ == "__main__":
    archive1 = Archive('one', 1)
    archive2 = Archive('two', 2)
    print(archive1)
