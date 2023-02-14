import unittest
from calc_iteration3 import Calculator3
class AdditionTest(unittest.TestCase):
    def test_add_positiveNumber(self):
        self.actual = Calculator3.addition(3,5)
        self.expected = 8
        self.assertEqual(self.actual,self.expected)
    def test_add_negativeNumber(self):
        self.actual = Calculator3.addition(-4,-8)
        self.expected = -12        
        self.assertEqual(self.actual,self.expected)

class SubtractionTest(unittest.TestCase):
    def test_sub_positiveNumber(self):
        self.actual = Calculator3.subtraction(5,4)
        self.expected = 1
        self.assertEqual(self.actual,self.expected)
    def test_sub_negativeNumber(self):
        self.actual = Calculator3.subtraction(-4,-8)
        self.expected = 4
        self.assertEqual(self.actual,self.expected)
        
class MultiplicationTest(unittest.TestCase):
    def test_multiply_positiveNumber(self):
        self.actual = Calculator3.multiplication(5,4)        
        self.expected = 20 
        self.assertEqual(self.actual,self.expected)
    def test_multiply_negativeNumber(self):
        self.actual = Calculator3.multiplication(-4,-4)        
        self.expected = 16 
        self.assertEqual(self.actual,self.expected)
        
class DivisionTest(unittest.TestCase):
    def test_division_positiveNumber(self):
        self.actual = Calculator3.division(10,5)
        self.expected = 2
        self.assertEqual(self.actual,self.expected)
    def test_division_negativeNumber(self):
        self.actual = Calculator3.division(-24,-2)
        self.expected = 12
        self.assertEqual(self.actual,self.expected)                        