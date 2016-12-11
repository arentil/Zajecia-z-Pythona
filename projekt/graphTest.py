#!/usr/bin/python
# -*- coding: utf-8 -*-
#kompilacja z python3

from graph import Graph
import unittest

class TestDijkstra(unittest.TestCase):
    
    def setUp(self): pass

    def test_addNode(self):
        g = Graph()
        g.addNode("A")
        self.assertEqual(g.nodes[0].letter, "A")
        self.assertEqual(len(g.nodes[0].nList), 0)
        
    def test_get(self):
        g = Graph()
        g.addNode("A"); g.addNode("B")
        self.assertTrue(g.get("A").letter == "A")
        self.assertFalse(g.get("A").letter == "B")

    def test_addNeighbor(self): #tez test_getNeighbors
        g = Graph()
        g.addNode("A"); g.addNode("B"); g.addNode("C")
        g.addNeighbor("A", "B", 10); g.addNeighbor("A", "C", 30)
        g.addNeighbor("B", "A", 10); g.addNeighbor("B", "C", 20)
        g.addNeighbor("C", "A", 30); g.addNeighbor("C", "B", 20)
        self.assertEqual(g.getNeighbors("A"), [("B", 10), ("C", 30)])
        self.assertEqual(g.getNeighbors("B"), [("A", 10), ("C", 20)])
        self.assertEqual(g.getNeighbors("C"), [("A", 30), ("B", 20)])
        
    def test_initialize(self):
        g = Graph()
        g.addNode("A"); g.addNode("B"); g.addNode("C")
        g.initialize("B")
        self.assertEqual(g.start, "B")
        self.assertEqual(g.get("B").fromStart, 0)
        self.assertTrue(g.get("A").fromStart == 100000 and g.get("A").prev == None)
        self.assertTrue(g.get("B").fromStart == 0 and g.get("B").prev == None)
        self.assertTrue(g.get("C").fromStart == 100000 and g.get("C").prev == None)
        
        
    '''
    Testuje graf:
        B---D
      / |\  |
     A  | \ |  F
      \ |  \| /
        C   E
    
    pionowe: 5, skośne 7
    ''' 
    def test_dijkstra(self):
        g = Graph()
        g.addNode("A"); g.addNode("B"); g.addNode("C")
        g.addNode("D"); g.addNode("E"); g.addNode("F")
        g.addNeighbor("A", "B", 7); g.addNeighbor("A", "C", 7)
        g.addNeighbor("B", "A", 7); g.addNeighbor("B", "C", 5); g.addNeighbor("B", "D", 5); g.addNeighbor("B", "E", 7)
        g.addNeighbor("C", "A", 7); g.addNeighbor("C", "B", 5);
        g.addNeighbor("D", "B", 5); g.addNeighbor("D", "E", 5)
        g.addNeighbor("E", "B", 7); g.addNeighbor("E", "D", 5); g.addNeighbor("E", "F", 7)
        g.addNeighbor("F", "E", 7)
        g.dijkstra("A")
        pList = []          #pobieram najkrotsze sciezki z kazdego wierzcholka do A
        for n in g.nodes:   # i laduje do listy list 
            if (n.letter == "A"): continue
            pnList = []
            node = n
            while node:
                pnList.append(node.letter)
                node = node.prev
            pList.append(pnList)
        # od B do A
        self.assertEqual(pList[0], ["B", "A"])
        #od C do A
        self.assertEqual(pList[1], ["C", "A"])
        # od D do A
        self.assertEqual(pList[2], ["D", "B", "A"])
        # od E do A
        self.assertEqual(pList[3], ["E", "B", "A"])
        # od F do A
        self.assertEqual(pList[4], ["F", "E", "B", "A"])

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie test
    
    
    
#self.assertEqual(,)
#self.assertTrue()