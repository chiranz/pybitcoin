from unittest import TestCase
from .point import Point
from .field_element import FieldElement


class PointTest(TestCase):
    def test_ne(self):
        a = Point(x=3, y=7, a=5, b=7)
        b = Point(x=18, y=77, a=5, b=7)

        self.assertTrue(a != b)
        self.assertFalse(a != a)

    def test_add0(self):
        a = Point(x=None, y=None, a=5, b=7)
        b = Point(x=3, y=7, a=5, b=7)
        c = Point(x=3, y=-7, a=5, b=7)

        self.assertEqual(a + b, b)
        self.assertEqual(b + a, b)
        self.assertEqual(b + c, a)

    def test_add1(self):
        a = Point(x=3, y=7, a=5, b=7)
        b = Point(x=-1, y=-1, a=5, b=7)
        self.assertEqual(a+b, Point(x=2, y=-5, a=5, b=7))

    def test_add2(self):
        a = Point(x=-1, y=-1, a=5, b=7)
        self.assertEqual(a+a, Point(x=18, y=77, a=5, b=7))
