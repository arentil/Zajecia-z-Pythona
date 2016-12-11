#!/usr/bin/python
# -*- coding: utf-8 -*-
#kompilacja z python3

from priorityqueue import PriorityQ
from time import time

#-------------------------- EDGE ---------------------------
class Edge:
    
    def __init__(self, toNode, weight):
        self.to = toNode    #edge
        self.w = weight     #weight of edge


#--------------------------- NODE ---------------------------
class Node:
    def __init__(self, c):
        self.letter = c
        self.nList = []     #list of neighbors
        self.prev = None    #previous
        self.fromStart = 0       #weight from start
        
        
#-------------------------- GRAPH ---------------------------        
class Graph:
    def __init__(self):
        self.nodes = []
        self.q = PriorityQ()
        self.start = ""
        
        
    def addNode(self, c):       #dodajemy do grafu wierzcholek o nazwie c
        self.nodes.append(Node(c))
        
        
    def get(self, c):           #zwracamy wierzcholek o nazwie c
        for n in self.nodes:
            if (n.letter == c):
                return n
            
        
    def addNeighbor(self, frm, to, weight):  
        #dodajemy krawędz o wadze weight of wierzcholka o nazwie frm do wierzcholka o nazwie to
        self.get(frm).nList.append(Edge(self.get(to), weight))
        
        
    def getNeighbors(self, node):   #funkcja zwracajaca liste par sasiadow
        rList = []                              # [(nazwa, waga), ...]
        for n in self.get(node).nList:
            rList.append((n.to.letter, n.w))
        return rList
    
    
    def initialize(self, start):        #inicjalizacja (dijkstry)
        self.start = start
        for n in self.nodes:
            n.fromStart = 100000
            n.prev = None
            if (n.letter == start):
                n.fromStart = 0
                
                
    def dijkstra(self, start):          #dijkstra
        t = time()
        self.initialize(start)
        self.q.push(self.get(start), self.get(start).fromStart)
        
        while (not self.q.empty()):
            u = self.q.pop()
            for n in u.nList:
                if (n.to.fromStart > (u.fromStart + int(n.w))):
                    n.to.fromStart = u.fromStart + int(n.w)
                    n.to.prev = u
                    self.q.push(n.to, n.to.fromStart)
        return ("Dijkstra time:  \t" + str(time() - t))
    
    
    def bellmanFord(self, start):
        t = time()
        self.initialize(start)
        for i in range(0, len(self.nodes) - 1):
            for u in self.nodes:
                for n in u.nList:
                    if (n.to.fromStart > (u.fromStart + int(n.w))):
                        n.to.fromStart = u.fromStart + int(n.w)
                        n.to.prev = u
        return ("Bellman-Ford time: \t" + str(time() - t))
        
    
    def getFromFile(self, filename):    #odczytujemy graf z pliku
        with open(filename, 'r') as f:
            line = f.readline()
            line = line.split()
            for nodeName in line:
                self.addNode(nodeName)
            edges = int(f.readline())
            for i in range(0, edges):
                line = f.readline()
                line = line.split()
                self.addNeighbor(line[0], line[1], line[2])    
        f.close()
        

    def writeToFile(self, filename):    #zapisujemy wyniki dijkstry do pliku
        with open(filename, 'w') as f:
            f.write("From every node to start node:\n\n")
            for n in self.nodes:
                if (n.letter == self.start):
                    continue
                temp = n
                while ((not temp.letter == self.start) and (not temp.prev == None)):
                    f.write(temp.letter + " -> ")
                    temp = temp.prev
                    
                f.write(self.start)
                f.write("   with total cost: " + str(n.fromStart) + "\n")
            f.write("\n")
            for n in self.nodes:
                f.write(n.letter + "\n")
                for u in n.nList:
                    f.write("\t-> " + u.to.letter + " \tcost: " + u.w + "\n")

                
        f.close()