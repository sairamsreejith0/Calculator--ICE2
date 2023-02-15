import unittest                                           #testcases to check addition and subtraction function
from calc_iteration1 import Calculator
class AdditionTest(unittest.TestCase):
    def test_add_positiveNumber(self):
        self.actual = Calculator.addition(3,5)
        self.expected = 8
        self.assertEqual(self.actual,self.expected)
    def test_add_negativeNumber(self):
        self.actual = Calculator.addition(-4,-8)
        self.expected = -12        
        self.assertEqual(self.actual,self.expected)

class SubtractionTest(unittest.TestCase):
    def test_sub_positiveNumber(self):
        self.actual = Calculator.subtraction(5,4)
        self.expected = 1
        self.assertEqual(self.actual,self.expected)
    def test_sub_negativeNumber(self):
        self.actual = Calculator.subtraction(-4,-8)
        self.expected = 4
        self.assertEqual(self.actual,self.expected)