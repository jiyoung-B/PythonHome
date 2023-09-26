# import pdb
# pdb.set_trace()

# def sum(x, y) :
#     return x + y

# a = 10
# b = 20
# c = sum(a, b)
# print(c)

import unittest
import myfunction

class MyTest(unittest.TestCase) :
    def test_sum(self) :
        self.assertEqual(myfunction.sum(2, 5), 7)
    def test_multiple(self) :
        self.assertEqual(myfunction.multiple(2, 5), 9)
    