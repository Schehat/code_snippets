import unittest
from unittest import result
import calc

# run in terminal:  python -m unittest <name of test file here test_calc.py>
# with the if __name__ == "main" block this will work as well: python test_calc.py


class TestCalc(unittest.TestCase):

    # methods need to be named test_*
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)

        # include edge cases
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)

        # arguments: Exception type, method without paranthesis,
        # required arguments seperated by comma
        # self.assertRaises(ValueError, calc.divide, 10, 0)
        # another option
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == "__main__":
    unittest.main()  # will run all tests
