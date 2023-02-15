import unittest
from calc_sprint1 import Calculator1
class AdditionTest(unittest.TestCase):
    def test_add_positiveNumber(self):
        self.actual = Calculator1.addition(3,5)
        self.expected = 8
        self.assertEqual(self.actual,self.expected)
    def test_add_negativeNumber(self):
        self.actual = Calculator1.addition(-4,-8)
        self.expected = -12        
        self.assertEqual(self.actual,self.expected)

class SubtractionTest(unittest.TestCase):
    def test_sub_positiveNumber(self):
        self.actual = Calculator1.subtraction(5,4)
        self.expected = 1
        self.assertEqual(self.actual,self.expected)
    def test_sub_negativeNumber(self):
        self.actual = Calculator1.subtraction(-4,-8)
        self.expected = 4
        self.assertEqual(self.actual,self.expected)