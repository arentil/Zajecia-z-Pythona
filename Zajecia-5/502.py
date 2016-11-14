#kompilacja z python3, plik testuje funkcje z pliku fracs.py
#!/usr/bin/python

import unittest
from fracs import *

class TestFractions(unittest.TestCase):
    
    def setUp(self):
        self.zero = [0,1]
        
    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([1, 2], [1, 10]), [3, 5])
        
    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([1, 2], [1, 10]), [2, 5])
        
    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [2, 3]), [2, 6])
        self.assertEqual(mul_frac([1, 2], [3, 10]), [3, 20])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(div_frac([1, 2], [1, 10]), [10, 2])

    def test_is_positive(self):
        self.assertEqual(is_positive([1, 2]), True)
        self.assertEqual(is_positive([-1,4]), False)

    def test_is_zero(self):
        self.assertEqual(is_zero([1, 2]), False)
        self.assertEqual(is_zero([0,5]), True)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1,2],[1,2]), 0)
        self.assertEqual(cmp_frac([1,2],[1,3]), 1)
        self.assertEqual(cmp_frac([-1,2],[1,3]), -1)

    def test_frac2float(self):
        self.assertEqual(frac2float([1,2]),0.5)
        self.assertEqual(frac2float([3,8]),0.375)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy