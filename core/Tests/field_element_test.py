import unittest
from ECC.Math.field_element import FieldElement


class FieldElementTest(unittest.TestCase):

    def test_ne(self):
        a = FieldElement(2, 31)
        b = FieldElement(2, 31)
        c = FieldElement(12, 31)
        self.assertEqual(a, b)
        self.assertTrue(a != c)
        self.assertFalse(a != b)

    def test_add(self):
        a = FieldElement(10, 31)
        b = FieldElement(25, 31)
        c = FieldElement(25, 41)
        self.assertEqual(a+b, FieldElement(4, 31))
        with self.assertRaises(ValueError):
            FieldElement(45, 31)


if __name__ == "__main__":
    unittest.main()
