import pytest

from task3 import Employee


@pytest.fixture
def emp():
    return Employee('Ivanov', 'Ivan', 'Ivanovich', 30, 'manager', 50_000)


def test_employee_full_name(emp):
    assert emp.full_name() == 'Ivanov Ivan Ivanovich'


def test_employee_birthday(emp):
    emp.birthday()
    assert emp.get_age() == 31


def test_employee_raise_salary(emp):
    emp.raise_salary(10)
    assert emp.salary == 55_000.0


def test_employee_str(emp, capsys):
    print(emp)
    captured_print = capsys.readouterr()
    assert captured_print.out == 'Ivanov Ivan Ivanovich (Manager)\n'


def test_employee_last_name_title(emp):
    assert emp.last_name == 'Ivanov'


if __name__ == "__main__":
    pytest.main(["--no-header", '-q', "--durations=0", 'Homework_14/task6.py'])