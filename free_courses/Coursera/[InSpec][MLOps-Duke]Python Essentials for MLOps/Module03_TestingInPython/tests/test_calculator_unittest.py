import unittest
from calculator import Calculator  

class TestCalculator(unittest.TestCase): 
    """
        Every test class must inherit from unittest.TestCase
        Individual test methods are defined by naming them with a 'test_' prefix.
    """
    def setUp(self):
        self.calc = Calculator()

    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtract_numbers(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-2, -3), 1)

    def test_multiply_numbers(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    def test_divide_normal(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(7, 3), 7/3)

    def test_divide_by_zero_returns_exception(self):
        result = self.calc.divide(5, 0)
        self.assertIsInstance(result, Exception)
        self.assertIsInstance(result, ZeroDivisionError)

    def test_divide_non_numeric_raises(self):
        result = self.calc.divide("a", 2)
        self.assertIsInstance(result, Exception)
        self.assertIsInstance(result, TypeError)

if __name__ == '__main__':
    unittest.main()
