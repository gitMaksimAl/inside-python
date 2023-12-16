# Создайте функцию, которая удаляет из текста все символы кроме букв латинского
# алфавита и пробелов. Возвращается строка в нижнем регистре.

from string import ascii_letters


def del_not_ascii(text: str) -> str:
    """
    >>> del_not_ascii('Hello World')
    'HelloWorld'
    >>> del_not_ascii('Hello, World!')
    'HelloWorld'
    >>> del_not_ascii('Hello Друг')
    'Hello'
    """
    chars = []
    for char in text:
        if char in ascii_letters:
            chars.append(char)
    return ''.join(chars)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
