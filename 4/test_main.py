import unittest
from main import funkcja_silni
from main import dodawanie
from main import odejmowanie
from main import pierwiastek



class TestFunkcjaSilni(unittest.TestCase):
    def testSilnia(self):
        # silnia <0
        self.assertAlmostEqual(funkcja_silni(1), 1)
        self.assertAlmostEqual(funkcja_silni(0), 1)

    def testValuesSilnia(self):
        self.assertRaises(ValueError, funkcja_silni, -2)

    def testTypesSilnia(self):
        self.assertRaises(TypeError, funkcja_silni, True)
        self.assertRaises(TypeError, funkcja_silni, 3 + 8j)
        self.assertRaises(TypeError, funkcja_silni, "kolo")


class TestDodawanie(unittest.TestCase):
    def testDodawanie(self):
        self.assertAlmostEqual(dodawanie(1, 1), 2)
        self.assertAlmostEqual(dodawanie(-2, 2), 0)

    def testTypeDodoawnie(self):
        self.assertRaises(TypeError, dodawanie, "kolo", 2)
        self.assertRaises(TypeError, dodawanie, True, False)

    def testValuesDodoawnie(self):
        self.assertRaises(ValueError, dodawanie, 2, 0)


class TestOdejmowanie(unittest.TestCase):
    def testOdejmowanie(self):
        self.assertAlmostEqual(odejmowanie(2, 2), 0)

    def testTypeOdodoawnie(self):
        self.assertRaises(TypeError, odejmowanie, "kolo", 2)
        self.assertRaises(TypeError, odejmowanie, True, False)

    def testValuesOdodoawnie(self):
        self.assertRaises(ValueError, odejmowanie, 2, -0.1)


class TestPierwiastek(unittest.TestCase):
    def testPierwiastek(self):
        self.assertAlmostEqual(pierwiastek(3, 27), 3)

    def testTypePierwiastek(self):
        self.assertRaises(TypeError, pierwiastek, 2, "sqrt")
        self.assertRaises(TypeError, pierwiastek, 'H', 27)

    def testValuePierwiastek(self):
        self.assertRaises(ValueError, pierwiastek, -2, 20)


if __name__ == "__main__":
    unittest.main()
