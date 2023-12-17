import pytest

from task2 import Rectangle, NegativeValueError


@pytest.fixture
def r1():
    return Rectangle(5)


@pytest.fixture
def r2():
    return Rectangle(3, 4)


@pytest.fixture
def negative_r1():
    return -5


def test_width(r1):
    assert r1.width == 5


def test_height(r2):
    assert r2.height == 4


def test_perimeter(r1):
    assert r1.perimeter() == 20


def test_area(r2):
    assert r2.area() == 12


def test_addition(r2):
    rect1 = Rectangle(5, 1)
    rect3 = rect1 + r2
    assert rect3.width == 6 and rect3.height == 7.0


def test_negative_width():
    with pytest.raises(NegativeValueError):
        Rectangle(-5)


def test_negative_height():
    with pytest.raises(NegativeValueError):
        Rectangle(5, -4)


def test_set_width(r1):
    r1.width = 10
    assert r1.width == 10


def test_set_negative_width(r1):
    with pytest.raises(NegativeValueError):
        r1.width = -5


def test_set_height(r2):
    r2.height = 6
    assert r2.height == 6


def test_set_negative_height(r2):
    with pytest.raises(NegativeValueError):
        r2.height = -6


def test_subtraction():
    rect1 = Rectangle(10, 4)
    rect2 = Rectangle(3, 1)
    rect3 = rect1 - rect2
    assert rect3.width == 7 and rect3.height == 3.0


def test_subtraction_negative_result():
    rect1 = Rectangle(3, 1)
    rect2 = Rectangle(10, 4)
    with pytest.raises(NegativeValueError):
        rect1 - rect2


def test_subtraction_same_perimeter(r2):
    rect1 = Rectangle(5, 1)
    rect3 = rect1 - r2
    assert rect3.width == 1 and rect3.height == 2.0


if __name__ == "__main__":
    pytest.main(["--no-header", '-q', "--durations=0", 'Homework_14/task5.py'])