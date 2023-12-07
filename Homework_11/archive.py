class Archive:

    __instance = None
    archive_text = None
    archive_number = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.archive_text = []
            cls.archive_number = []
        return cls.__instance

    def __init__(self, string: str, number: int):
        self.text = string
        self.number = number
        self.archive_text.append(self.text)
        self.archive_number.append(self.number)

    def __str__(self):
        return f"Text is {self.text} and number is {self.number}." \
               f" Also {self.archive_text} and {self.archive_number}"

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'


if __name__ == "__main__":
    archive = Archive("One", 1)
    print(archive)
    print(repr(archive))
    print()
    archive2 = Archive("Two", 2)
    print(archive2)
