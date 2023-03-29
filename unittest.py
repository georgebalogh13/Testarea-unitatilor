import unittest


def division(a, b):
    return a/b
    

class testDivisionFromNumbers(unittest.TestCase): 
    def test_division(self):
        with self.assertRaises(ZeroDivisionError):
         division(10,0)
         
    def test_StringFristParameter(self):
        with self.assertRaises(TypeError):
         division("31", 4)
         
    def test_StringSecondParameter(self):
        with self.assertRaises(TypeError):
         division(10,"3")
         
def suite():
    test_suite = unittest.TestSuite() 
    test_suite.addTest(unittest.makeSuite(testDivisionFromNumbers))
    return test_suite        
         
suite = suite()

runner=unittest.TextTestRunner() 
runner.run(suite)
