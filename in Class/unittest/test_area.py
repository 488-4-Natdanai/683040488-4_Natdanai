# test_area.py
import unittest
from area import calculate_area

class TestAreaCalculation(unittest.TestCase):
    def test_positive_numbers(self):
        # Tests with positive numbers (put in several tests here for different cases)
        self.assertEqual(calculate_area(6, 7), 42)
        self.assertEqual(calculate_area(7, 6), 42)
        self.assertEqual(calculate_area(1, 1), 1)
        self.assertEqual(calculate_area(5, 99.99), 499.95)

    def test_zero(self):
        self.assertEqual(calculate_area(4, 0), 0)
        self.assertEqual(calculate_area(0, 4), 0)
        self.assertEqual(calculate_area(0, 0), 0)

    def test_negative_numbers(self):
        # Test with negative numbers (put in several tests here for different cases)
        with self.assertRaises(ValueError):
            calculate_area(-20, 100)
        with self.assertRaises(ValueError):
            calculate_area(20, -100)
        with self.assertRaises(ValueError):
            calculate_area(-20, -100)

    def test_type(self):
        with self.assertRaises(TypeError):
            calculate_area("a",2)
        with self.assertRaises(TypeError):
            calculate_area(2,"a")
        with self.assertRaises(TypeError):
            calculate_area("a","a")
        with self.assertRaises(TypeError):
            calculate_area(["a","a"], ["100"])


if __name__ == '__main__':
    unittest.main()