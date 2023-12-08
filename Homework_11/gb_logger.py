from datetime import datetime


class MyStr(str):

    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        return instance

    def __init__(self, value: str, author: str):
        self.author = author
        self.time = f"{datetime.today():%Y-%m-%d %H:%M}"

    def __str__(self):
        string = f" (Автор: {self.author}, " \
               f"Время создания: {self.time})"
        return self + string

    def __repr__(self):
        return "MyStr('" + self + f"', '{self.author}')"


if __name__ == "__main__":
    my_str = MyStr("Primer teksta", "Maksim")
    # eval(f"x = {repr(my_str)}")
    # print(x)
    print(my_str, repr(my_str), sep='\n')
