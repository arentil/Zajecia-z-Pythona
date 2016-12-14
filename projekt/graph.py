#!/usr/bin/python
# -*- coding: utf-8 -*-
#kompilacja z python3

from priorityqueue import PriorityQ
from time import time

#-------------------------- EDGE ---------------------------
class Edge:
    '''klasa reprezentująca krawędź jak dla grafu skierowanego'''
    
    def __init__(self, toNode, weight):
        self.to = toNode    #krawędź która prowadzi do wierzchołka "to"
        self.w = weight     #waga krawędzi


#--------------------------- NODE ---------------------------
class Node:
    '''klasa reprezentująca wierzchołek'''
    
    def __init__(self, nodeName):
        self.name = nodeName    #nazwa wierzchołka
        self.eList = []         #lista krawędzi(skierowanych) do sąsiadów (edgeList)
        self.previous = None    #poprzedik
        self.distFromStart = 0  #waga od wierzchołka startowego
        
        
#-------------------------- GRAPH ---------------------------        
class Graph:
    def __init__(self):
        self.nodes = []     #lista wierzchołków
        self.start = ""     #pomocniczo nazwa wierzchołka startowego
        
        
    def addNode(self, nodeName):
        '''tworzymy wierzchołek i dodajemy go do grafu o ile o takiej nazwie już nie istnieje'''
        for node in self.nodes:
            if (node.name == nodeName):
                print("Próba stworzenia istniejącego wierzchołka!")
                return
        self.nodes.append(Node(nodeName))        
        
        
    def getNode(self, nodeName):           
        '''funkcja zwracająca wierzchołek o nazwie nodeName, jeżeli nie ma takiego, zwraca None'''
        for node in self.nodes:
            if (node.name == nodeName):
                return node
        return None
            
        
    def addNeighbor(self, fromNode, toNode, weight):  
        '''dodajemy krawędz o wadze weight z wierzcholka o nazwie fromNode do wierzcholka o nazwie toNode'''
        fromN = self.getNode(fromNode)
        toN = self.getNode(toNode)
        if ((not fromN == None) and (not toN == None)):
            fromN.eList.append(Edge(toN, weight))
        else:
            print("Próba dodania krawędzi między nieistniejącymi wierzchołkami!")
        
    def getStringNeighbors(self, node):
        '''funkcja(pomocnicza dla wyświetlania) zwraca listę par sąsiadów [(sąsiad1, waga), (sąsiad2, waga), ...]'''
        rList = []
        for edge in self.getNode(node).eList:
            rList.append((edge.to.name, edge.w))
        return rList
    
    
    def initialize(self, start):        
        '''inicjalizacja (dijkstry i bellmana-forda)'''
        self.start = start
        for node in self.nodes:
            node.distFromStart = 100000
            node.previous = None
            if (node.name == start):
                node.distFromStart = 0
                
                
    def dijkstra(self, start):
        ''' algorytm dijkstry'''
        q = PriorityQ()
        t = time()
        self.initialize(start)
        q.push(self.getNode(start), self.getNode(start).distFromStart)
        
        while (not q.empty()):
            node = q.pop()
            for edge in node.eList:
                if (edge.to.distFromStart > (node.distFromStart + int(edge.w))):
                    edge.to.distFromStart = node.distFromStart + int(edge.w)
                    edge.to.previous = node
                    q.push(edge.to, edge.to.distFromStart)
        return ("Czas Dijkstry:  \t" + str(time() - t))
    
    
    def bellmanFord(self, start):
        '''algorytm bellmana-forda dla porównania czasu z dijkstrą'''
        t = time()
        self.initialize(start)
        for i in range(0, len(self.nodes) - 1):
            for node in self.nodes:
                for edge in node.eList:
                    if (edge.to.distFromStart > (node.distFromStart + int(edge.w))):
                        edge.to.distFromStart = node.distFromStart + int(edge.w)
                        edge.to.previous = node
        return ("Czas Bellmana-Forda: \t" + str(time() - t))
        
    
    def getFromFile(self, filename):    
        '''odczytujemy graf z pliku'''
        with open(filename, 'r') as f:
            for line in f:
                line = line.split()
                if (self.getNode(line[0]) == None):
                    self.addNode(line[0])
                if (self.getNode(line[1]) == None):
                    self.addNode(line[1])
                self.addNeighbor(line[0], line[1], line[2]) 
        f.close()
        

    def writeToFile(self, filename):    
        '''zapisujemy graf do pliku'''
        with open(filename, 'w') as f:
            f.write("Od każdego wierzchołka do wierzchołka początkowego:\n\n")
            for node in self.nodes:
                if (node.name == self.start):
                    continue
                temp = node
                while ((not temp.name == self.start) and (not temp.previous == None)):
                    f.write(temp.name + " -> ")
                    temp = temp.previous
                    
                f.write(self.start)
                f.write("   koszt całkowity: " + str(node.distFromStart) + "\n")
            f.write("\n")
            f.write("Zawartość list sąsiedztwa każdego wierzchołka:\n\n")
            for node in self.nodes:
                f.write(node.name + "\n")
                for edge in node.eList:
                    f.write("\t-> " + edge.to.name + " \tkoszt: " + edge.w + "\n")
        f.close()