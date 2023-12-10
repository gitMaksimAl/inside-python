from pprint import pprint
from pathlib import Path
from csv import reader, QUOTE_NONNUMERIC, Sniffer


class Subjects:

    def __set_name__(self, owner, name):
        self._param_name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self._param_name)

    def __set__(self, instance, value):
        if not isinstance(value, dict):
            raise ValueError("Need grades like: dict[str, dict[str, list[int]]")
        setattr(instance, self._param_name, value)

    def __del__(self):
        del self._param_name


class StudentName:

    def __set_name__(self, owner, name):
        self._param_name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self._param_name)

    @staticmethod
    def _validate(value: str) -> None:
        if not all(map(str.isalpha, value.split(' '))) \
                or not all(map(str.istitle, value.split(' '))):
            print("ФИО должно состоять только из букв и"
                  " начинаться с заглавной буквы")
            raise ValueError

    def __set__(self, instance, value):
        StudentName._validate(value)
        setattr(instance, self._param_name, value)

    def __del__(self):
        del self._param_name


class Student:
    _MIN_GRADE = 2
    _MAX_GRADE = 5
    _MIN_TEST_GRADE = 0
    _MAX_TEST_GRADE = 100

    name = StudentName()
    subjects = Subjects()

    def __init__(self, name: str, subjects_file: str):
        self.name = name
        self._data_file = Path(subjects_file)
        if not self._data_file.is_file():
            raise ValueError("Can't find file")
        self.subjects = Student.load_subjects(self._data_file)

    @staticmethod
    def load_subjects(file: Path):
        with file.open('r', encoding='utf-8', newline='') as f:
            sample = f.read(1024)
            dialect = Sniffer().sniff(sample)
            f.seek(0)
            csv_reader = reader(f, dialect=dialect, quoting=QUOTE_NONNUMERIC)
            headers = next(csv_reader)
            subjects = {}
            for key in headers:
                subjects.setdefault(key, {})
                subjects[key].setdefault("grades", [])
                subjects[key].setdefault("test_grades", [])
            grades = [list(i) for i in zip(*csv_reader)]
            for k, v in zip(subjects.values(), grades):
                for grade in v:
                    k["grades"].append(int(grade))
        return subjects

    def add_grade(self, subject: str, grade: int) -> bool:
        if isinstance(grade, int) \
                and (Student._MIN_GRADE <= grade <= Student._MAX_GRADE):
            self.subjects[subject]["grades"].append(grade)
            return True
        print("Оценка должна быть целым числом от 2 до 5")
        return False

    def add_test_score(self, subject: str, test_score: int) -> bool:
        target = self.subjects.get(subject)
        if not target:
            print(f"Предмет {subject} не найден")
            return False
        if isinstance(test_score, int) \
                and Student._MIN_TEST_GRADE <= test_score \
                <= Student._MAX_TEST_GRADE:
            target["test_grades"].append(test_score)
            return True
        print("Результат теста должен быть целым числом от 0 до 100")
        return False

    def get_average_test_score(self, subject: str) -> float:
        total = sum(self.subjects[subject]["test_grades"])
        try:
            return round(total / len(self.subjects[subject]["test_grades"]), 1)
        except ZeroDivisionError:
            return 0.0

    def get_average_grade(self) -> float:
        total = {}
        try:
            for sub, grades in self.subjects.items():
                total[sub] = sum(grades["grades"]) / len(grades["grades"])
            return round(sum(total.values()) / len(total), 1)
        except ZeroDivisionError:
            return 0.0

    def __str__(self):
        subjects = ', '.join(self.subjects.keys())
        return f"Студент: {self.name}\nПредметы: {subjects}"


if __name__ == "__main__":
    student = Student("Иван Иванов", "subjects.csv")
    student2 = Student("Arsen Petrov", "subjects.csv")

    print(student)
    student.add_grade("Algebra", 4)
    student.add_test_score("Algebra", 85)
    student.add_grade("Sport", 5)
    student.add_test_score("Sport", 92)

    student2.add_grade("Algebra", 5)
    student2.add_grade("Phisics", 5)
    student2.add_grade("Sport", 5)
    student2.add_grade("Sport", 5)
    student.add_test_score("Sport", 99)
    student.add_test_score("Algebra", 44)
    print(student)
    print(student2)

    pprint(student.subjects)
    print()
    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")

    average_test_score = student.get_average_test_score("Algebra")
    print(f"Средний результат по тестам по математике: {average_test_score}")
