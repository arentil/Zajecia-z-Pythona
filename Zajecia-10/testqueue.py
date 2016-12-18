#!/usr/bin/python
# -*- coding: utf-8 -*-
#kompilacja z python3

import unittest
from queue import *

class TestQueue(unittest.TestCase):
    
    def setUp(self): pass

    def test_is_empty(self):
        q = Queue(2)
        self.assertTrue(q.is_empty())
        q.put(1)
        self.assertFalse(q.is_empty())
        q.get()
        self.assertTrue(q.is_empty())
        
    def test_is_full(self):
        q = Queue(2)
        self.assertFalse(q.is_full())
        q.put(1)
        q.put(2)
        self.assertTrue(q.is_full())
        
    def test_put(self):
        q = Queue(3)
        q.put(1)
        q.put(2)
        q.put(3)
        try:
            q.put(3)
        except Exception as e:
            self.assertEqual(str(e), "Queue full!")

    def test_get(self):
        q = Queue(3)
        q.put(1)
        q.put(2)
        self.assertEqual(q.get(), 1)
        self.assertEqual(q.get(), 2)
        try:
            q.get()
        except Exception as e:
            self.assertEqual(str(e), "Queue empty!")

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie test