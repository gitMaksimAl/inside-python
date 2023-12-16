import unittest

from Lesson_11.task2 import RectangleExtend


class TestRectangles(unittest.TestCase):

    def setUp(self) -> None:
        self.r1 = RectangleExtend(3, 3)
        self.r2 = RectangleExtend(4, 7)

    def test_one(self):
        self.assertEqual(RectangleExtend(3, 3), self.r1)
        self.assertEqual(RectangleExtend(4, 7), self.r2)

    def test_two(self):
        self.assertEqual(self.r1.area(), 9)
        self.assertEqual(self.r2.area(), 28)

    def test_three(self):
        self.assertEqual(self.r1.perimeter(), 12)
        self.assertEqual(self.r2.perimeter(), 22)

    def test_four(self):
        self.assertGreater(self.r2, self.r1)
        self.assertLess(self.r1, self.r2)
