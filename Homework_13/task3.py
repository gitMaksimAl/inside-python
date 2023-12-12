class InvalidNameError(ValueError):

    def __init__(self, value):
        super(InvalidNameError, self).__init__(f"Invalid name value: {value}.")


class InvalidAgeError(ValueError):

    def __init__(self, value):
        super(InvalidAgeError, self).__init__(f"Invalid age value: {value}.")


class InvalidIdError(ValueError):

    def __init__(self, value):
        super(InvalidIdError, self).__init__(f"Invalid id value{value}.")


class TrueName:

    def __set_name__(self, owner, name):
        self.__name = f"_{name}"

    def __set__(self, instance, value: str):
        if value != "" and not (value.istitle() and value.isalpha()):
            raise InvalidNameError(value)
        if value == "" and self.__name != "_last_name":
            raise InvalidNameError(value)
        setattr(instance, self.__name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.__name)


class TrueAge:

    def __set_name__(self, owner, name):
        self.__name = f"_{name}"

    def __set__(self, instance, value: int | float):
        if value <= Person.MIN_AGE or value > Person.MAX_AGE:
            raise InvalidAgeError(value)
        setattr(instance, self.__name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.__name)


class Id:

    def __set_name__(self, owner, name):
        self.__name = f"_{name}"

    def __set__(self, instance, value: int | float):
        if value <= 0:
            raise InvalidIdError
        setattr(instance, self.__name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.__name)


class Person:

    MAX_AGE = 105
    MIN_AGE = 0
    name = TrueName()
    last_name = TrueName()
    sur_name = TrueName()
    age = TrueAge()

    def __init__(self, last_name: str, first_name: str,
                 middle_name: str, age: int):
        self.name = first_name
        self.sur_name = middle_name
        self.last_name = last_name
        self.age = age

    def birthday(self):
        if self.age < Person.MAX_AGE:
            self.age += 1

    def __getattr__(self, item):
        return None

    def __repr__(self):
        return f"Person({self.last_name}, {self.name}, " \
               f"{self.sur_name}, {self.age})"


class Employee(Person):

    employee_id = Id()

    def __init__(self, last_name: str, first_name: str, middle_name: str,
                 age: int, employee_id: int):
        super().__init__(last_name, first_name, middle_name, age)
        self.employee_id = employee_id

    def __getattr__(self, item):
        return None

    def get_level(self):
        return sum(int(i) for i in str(self.employee_id))

    def __repr__(self):
        return f"Employee({self.last_name}, {self.name}, " \
               f"{self.sur_name}, {self.age}, {self.employee_id})"


if __name__ == "__main__":
    person1 = Person("De", "John", "Doe", 30)
    print(person1)
    employee1 = Employee("", "Bob", "Marley", 30, 333)
    print(employee1)
    print(isinstance(employee1, Person))
