#!/usr/bin/python
# -*- coding: utf-8 -*-
#kompilacja z python3

from graph import Graph
import unittest

class TestDijkstra(unittest.TestCase):
    
    def setUp(self): pass

    def test_addNode(self):
        '''test metody addNode'''
        graph = Graph()
        graph.addNode("A")
        self.assertEqual(graph.nodes[0].name, "A")
        self.assertEqual(len(graph.nodes[0].eList), 0)
        
    def test_getNode(self):
        '''test metody getNode'''
        graph = Graph()
        graph.addNode("A"); graph.addNode("B")
        self.assertTrue(graph.getNode("A").name == "A")
        self.assertFalse(graph.getNode("A").name == "B")

    def test_addNeighbor(self):
        '''test metody addNeighbors'''
        graph = Graph()
        graph.addNode("A"); graph.addNode("B"); graph.addNode("C")
        graph.addNeighbor("A", "B", 10); graph.addNeighbor("A", "C", 30)
        graph.addNeighbor("B", "A", 10); graph.addNeighbor("B", "C", 20)
        graph.addNeighbor("C", "A", 30); graph.addNeighbor("C", "B", 20)
        self.assertEqual(graph.getStringNeighbors("A"), [("B", 10), ("C", 30)])
        self.assertEqual(graph.getStringNeighbors("B"), [("A", 10), ("C", 20)])
        self.assertEqual(graph.getStringNeighbors("C"), [("A", 30), ("B", 20)])
        
    def test_initialize(self):
        '''test metody initialize'''
        graph = Graph()
        graph.addNode("A"); graph.addNode("B"); graph.addNode("C")
        graph.initialize("B")
        self.assertEqual(graph.start, "B")
        self.assertEqual(graph.getNode("B").distFromStart, 0)
        self.assertTrue(graph.getNode("A").distFromStart == 100000 and graph.getNode("A").previous == None)
        self.assertTrue(graph.getNode("B").distFromStart == 0 and graph.getNode("B").previous == None)
        self.assertTrue(graph.getNode("C").distFromStart == 100000 and graph.getNode("C").previous == None)
        
        
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
        '''test algorytmu dijkstry'''
        graph = Graph()
        graph.addNode("A"); graph.addNode("B"); graph.addNode("C")
        graph.addNode("D"); graph.addNode("E"); graph.addNode("F")
        graph.addNeighbor("A", "B", 7); graph.addNeighbor("A", "C", 7)
        graph.addNeighbor("B", "A", 7); graph.addNeighbor("B", "C", 5); graph.addNeighbor("B", "D", 5); graph.addNeighbor("B", "E", 7)
        graph.addNeighbor("C", "A", 7); graph.addNeighbor("C", "B", 5);
        graph.addNeighbor("D", "B", 5); graph.addNeighbor("D", "E", 5)
        graph.addNeighbor("E", "B", 7); graph.addNeighbor("E", "D", 5); graph.addNeighbor("E", "F", 7)
        graph.addNeighbor("F", "E", 7)
        graph.dijkstra("A")
        pList = []          #pobieram najkrotsze sciezki z kazdego wierzcholka do A
        for node in graph.nodes:   # i laduje do listy list 
            if (node.name == "A"): continue
            pnList = []
            temp = node
            while temp:
                pnList.append(temp.name)
                temp = temp.previous
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