import unittest
from main import circle_area
from math import pi
from main import funkcja_silni
from main import same_number


class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # radius >=0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1 * 2)

    def test_values(self):
        # value error are necessary
        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):
        # type error are necessary
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, 3 + 8j)
        self.assertRaises(TypeError, circle_area, "kolo")


class TestFunkcjaSilni(unittest.TestCase):
    def test_silnia(self):
        # silnia <0
        self.assertAlmostEqual(funkcja_silni(0), 1)
        self.assertAlmostEqual(funkcja_silni(-1), None)

    def test_values(self):
        # value error are necessary
        self.assertRaises(ValueError, funkcja_silni, -2)

    def test_types(self):
        # type error are necessary
        self.assertRaises(TypeError, funkcja_silni, True)
        self.assertRaises(TypeError, funkcja_silni, 3 + 8j)
        self.assertRaises(TypeError, funkcja_silni, "kolo")


class TestSameNumbers(unittest.TestCase):
    def test_expected_value(self):
        self.assertEquals(same_number(2), False)
        self.assertEquals(same_number(2), True)

    def test_types(self):
        self.assertRaises(TypeError, same_number, True)
        self.assertRaises(TypeError, same_number, 3 + 8j, None)
        self.assertRaises(TypeError, same_number, "kolo", 3)
