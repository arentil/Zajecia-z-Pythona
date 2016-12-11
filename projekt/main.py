#!/usr/bin/python
# -*- coding: utf-8 -*-
#kompilacja z python3

from graph import Graph


g = Graph()

while (True):
    choise = int(input("Skąd chcesz wczytać dane?\n\t1) maly graf polski\n\t2) duży graf polski\n\t3) wlasny graf\n\tWpisz 1, 2 lub 3: "))
    if (choise == 1):
        g.getFromFile("gpsmall.txt")
        break
    
    elif (choise == 2):
        g.getFromFile("gpbig.txt")
        break
    
    elif (choise == 3):
        print("\nWpisuj nazwy wierzchołków do dodania(Enter kończy):")
        node = input()
        while (not node == ""):
            g.addNode(node)
            node = input()
            
        print("\nDopisuj sąsiadów do wierzchołka w sposób(Enter kończy):")
        print("OD_DO_WAGA  (gdzie _ zastąp spacją):")
        neighbors = input()
        while (not neighbors == ""):
            L = neighbors.split()
            g.addNeighbor(L[0], L[1], L[2])
            neighbors = input()
        break
    
    else:
        print("Niewlaściwy wybor!")
    

start = input("Podaj wierzcholek startowy: ")
print(g.dijkstra(start))
g.writeToFile("resultDijkstra.txt")
print(g.bellmanFord(start))
g.writeToFile("resultBellmanFord.txt")
print("Wyniki zostaly zapisane w plikach:\nresultDijkstra.txt\nresultBellmanFord.txt")