import unittest

from unittest import TestCase

from ECC.Math.point import Point
from ECC.Math.field_element import FieldElement


class ECCTest(TestCase):

    def test_on_curve(self):
        prime = 223
        a = FieldElement(0, prime)
        b = FieldElement(7, prime)
        valid_points = ((192, 105), (17, 56), (1, 193))
        invalid_points = ((200, 119), (42, 99))

        for x_raw, y_raw in valid_points:
            x = FieldElement(x_raw, prime)
            y = FieldElement(y_raw, prime)
            # Throws no error
            Point(x, y, a, b)
        for x_raw, y_raw in invalid_points:
            x = FieldElement(x_raw, prime)
            y = FieldElement(y_raw, prime)

            with self.assertRaises(ValueError):
                Point(x, y, a, b)

    def test_add(self):
        prime = 223
        a = FieldElement(0, prime)
        b = FieldElement(7, prime)
        additions = (
            (192, 105, 17, 56, 170, 142),
            (47, 71, 117, 141, 60, 139),
            (143, 98, 76, 66, 47, 71),
        )
        for item in additions:
            x1 = FieldElement(item[0], prime)
            y1 = FieldElement(item[1], prime)
            x2 = FieldElement(item[2], prime)
            y2 = FieldElement(item[3], prime)
            x3 = FieldElement(item[4], prime)
            y3 = FieldElement(item[5], prime)
            p1 = Point(x1, y1, a, b)
            p2 = Point(x2, y2, a, b)
            p3 = Point(x3, y3, a, b)

            self.assertEqual(p1+p2, p3)


if __name__ == "__main__":

    unittest.main()
