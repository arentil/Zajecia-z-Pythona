#!/usr/bin/python
# -*- coding: utf-8 -*-
#kompilacja z python3

class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self, *arguments):
        self.length = 0         # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None
        for item in arguments:
            self.insert_head(item)

    def __str__(self):      #funkcja pomocnicza aby łatwiej wyświetlać
        node = self.head
        ret = "["
        while (node):
                if (not node.next):
                        ret += str(node.data)
                else:
                        ret += str(node.data) + ", "
                node = node.next
        return ret + "]"

    def is_empty(self):
        return self.length == 0

    def count(self):      # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, data):    # algorytm klasy O(1)
        node = Node(data)
        if self.length == 0:
            self.head = self.tail = node
        else:                   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        self.length = self.length + 1

    def insert_tail(self, data):    # algorytm klasy O(1)
        node = Node(data)
        if self.length == 0:
            self.head = self.tail = node
        else:                   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        self.length = self.length + 1

    def remove_head(self):          # algorytm klasy O(1)
        if self.length == 0:
            raise Exception("pusta lista")
        node = self.head
        self.head = self.head.next
        self.length = self.length - 1
        if self.length == 0:   # zabezpieczenie
            self.tail = None
        return node.data
    
    def reverse(self):         #metoda odwracająca listę
        before = None
        after = self.head
        while (after):
            node = after.next
            after.next = before
            before = after
            after = node
        self.head = before
    
L = SingleList(24, 732, 24, 72, 23, 78)
print(L)
L.reverse()
print(L)