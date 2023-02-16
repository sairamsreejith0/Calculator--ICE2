import unittest  # import unittest to use testing functions
from calc import Calculator  # importing class Calculator from calc.py


# inheriting unittest.Testcase class to create a test class
class AdditionTest(unittest.TestCase):
    # function to check addition function with positive numbers
    def test_add_positiveNumber(self):
        # passing 2 values to add function and storing in variable named actual
        self.actual = Calculator.addition(3, 5)
        self.expected = 8  # provide expected value to get when the 2 numbers are added
        # assertEqual function checks whether actual and expected values are same if yes it returns true else false
        self.assertEqual(self.actual, self.expected)

    def test_add_negativeNumber(self):
        # similar to previous function this function is used to check for negative numbers
        self.actual = Calculator.addition(-4, -8)
        self.expected = -12
        self.assertEqual(self.actual, self.expected)


class SubtractionTest(unittest.TestCase):
    def test_sub_positiveNumber(self):
        # testcase to check subtraction for positive values
        self.actual = Calculator.subtraction(5, 4)
        self.expected = 1
        self.assertEqual(self.actual, self.expected)

    def test_sub_negativeNumber(self):
        # testcase to check subtraction for negative values
        self.actual = Calculator.subtraction(-4, -8)
        self.expected = 4
        self.assertEqual(self.actual, self.expected)


class MultiplicationTest(unittest.TestCase):
    def test_multiply_positiveNumber(self):
        # testcase to check multiplication for positive values
        self.actual = Calculator.multiplication(5, 4)
        self.expected = 20
        self.assertEqual(self.actual, self.expected)

    def test_multiply_negativeNumber(self):
        # testcase to check multiplication for negative values
        self.actual = Calculator.multiplication(-4, -4)
        self.expected = 16
        self.assertEqual(self.actual, self.expected)
