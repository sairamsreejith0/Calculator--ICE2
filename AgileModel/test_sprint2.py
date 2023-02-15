import unittest                                           #sprint2 testcases for addition and subtraction
from calc_sprint2 import Calculator2
class MultiplicationTest(unittest.TestCase):
    def test_multiply_positiveNumber(self):
        self.actual = Calculator2.multiplication(5,4)        
        self.expected = 20 
        self.assertEqual(self.actual,self.expected)
    def test_multiply_negativeNumber(self):
        self.actual = Calculator2.multiplication(-4,-4)        
        self.expected = 16 
        self.assertEqual(self.actual,self.expected)
class DivisionTest(unittest.TestCase):
    def test_division_positiveNumber(self):
        self.actual = Calculator2.division(10,5)
        self.expected = 2
        self.assertEqual(self.actual,self.expected)
    def test_division_negativeNumber(self):
        self.actual = Calculator2.division(-24,-2)
        self.expected = 12
        self.assertEqual(self.actual,self.expected)                