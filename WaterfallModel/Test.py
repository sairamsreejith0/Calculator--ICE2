import unittest                                  #import unittest to use testing functions
from calc import Calculator                      #importing class Calculator from calc.py 
class AdditionTest(unittest.TestCase):           #inheriting unittest.Testcase class to create a test class
    def test_add_positiveNumber(self):           #function to check addition function with positive numbers
        self.actual = Calculator.addition(3,5)   #passing 2 values to add function and storing in variable named actual
        self.expected = 8                        #provide expected value to get when the 2 numbers are added
        self.assertEqual(self.actual,self.expected) #assertEqual function checks whether actual and expected values are same if yes it returns true else false
    def test_add_negativeNumber(self): 
        self.actual = Calculator.addition(-4,-8)         #similar to previous function this function is used to check for negative numbers
        self.expected = -12        
        self.assertEqual(self.actual,self.expected)

class SubtractionTest(unittest.TestCase):
    def test_sub_positiveNumber(self):
        self.actual = Calculator.subtraction(5,4)           #testcase to check subtraction for positive values
        self.expected = 1
        self.assertEqual(self.actual,self.expected)
    def test_sub_negativeNumber(self):
        self.actual = Calculator.subtraction(-4,-8)         #testcase to check subtraction for negative values
        self.expected = 4
        self.assertEqual(self.actual,self.expected)
        
class MultiplicationTest(unittest.TestCase):
    def test_multiply_positiveNumber(self):
        self.actual = Calculator.multiplication(5,4)            #testcase to check multiplication for positive values
        self.expected = 20 
        self.assertEqual(self.actual,self.expected)
    def test_multiply_negativeNumber(self):
        self.actual = Calculator.multiplication(-4,-4)          #testcase to check multiplication for negative values
        self.expected = 16 
        self.assertEqual(self.actual,self.expected)    
            
            

    

