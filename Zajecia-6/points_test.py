#kompilacja z python3

import unittest
from points import *

class TestPoints(unittest.TestCase):

    def setUp(self): pass
        
    def test_str_frac(self):
        self.assertEqual(str(Point(55,22)), "(55, 22)")
        
    def test_eq_frac(self):
        self.assertTrue(Point(1,2) == Point(1,2))
        self.assertFalse(Point(2,2) == Point(1,2))
        
    def test_ne_frac(self):
        self.assertFalse(Point(1,2) != Point(1,2))
        self.assertTrue(Point(2,2) != Point(1,2))
        
    def test_add_frac(self):
        self.assertEqual(Point(55,22)+Point(3,7), Point(58,29))
        
    def test_sub_frac(self):
        self.assertEqual(Point(55,22)-Point(3,7), Point(52,15))
        
    def test_mul_frac(self):
        self.assertEqual(Point(2,3)*Point(3,8), 30)
        
    def test_cross_frac(self):
        self.assertEqual(Point(2,3).cross(Point(3,8)), 7)
        
    def test_length_frac(self):
        self.assertEqual(Point(3,4).length(), 5)
        
    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie test