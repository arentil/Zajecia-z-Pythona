#!/usr/bin/python
# -*- coding: utf-8 -*-
#kompilacja z python3

from graph import Graph


graph = Graph()

while (True):
    parsed = False
    while not parsed:
        try:
            choise = int(input("Skąd chcesz wczytać dane?\n\t1) maly graf polski\n\t2) duży graf polski\n\t3) wlasny graf\n\tWpisz 1, 2 lub 3: "))
            parsed = True
        except ValueError:
            print("Należy pocać cyfrę!")
        
    if (choise == 1):
        graph.getFromFile("graphSmall.txt")
        break
    
    elif (choise == 2):
        graph.getFromFile("graphBig.txt")
        break
    
    elif (choise == 3):
        print("\nWpisuj krawędzie wierzchołków w sposób(Enter kończy):")
        print("\"OdWierzchołka DoWierzchołka Waga\"  (np \"A B 5\"):")
        edge = input()
        while (not edge == ""):
            L = edge.split()
            if (graph.getNode(L[0]) == None):
                graph.addNode(L[0])
            if (graph.getNode(L[1]) == None):
                graph.addNode(L[1])
            graph.addNeighbor(L[0], L[1], L[2]) 
            edge = input()
        break
    else:
        print("Niewłaściwy wybor!")
    

start = input("Podaj wierzchołek startowy: ")
while (graph.getNode(start) == None):
    print("Podałeś nieistniejący wierzchołek!")
    start = input("Podaj wierzchołek startowy: ")
print(graph.dijkstra(start))
graph.writeToFile("resultDijkstra.txt")
print(graph.bellmanFord(start))
graph.writeToFile("resultBellmanFord.txt")
print("Wyniki zostały zapisane w plikach:\nresultDijkstra.txt\nresultBellmanFord.txt")