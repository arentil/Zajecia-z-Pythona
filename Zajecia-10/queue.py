#!/usr/bin/python
# -*- coding: utf-8 -*-
#kompilacja z python3

#zadanie 10.4 (queue) implementacja tablicowa

class Queue:

    def __init__(self, size=5):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None] 
        self.head = 0           # pierwszy do pobrania 
        self.tail = 0           # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def put(self, data):
        if (self.is_full()):
            raise Exception("Queue full!")
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if (self.is_empty()):
            raise Exception("Queue empty!")
        data = self.items[self.head]
        self.items[self.head] = None      # usuwam referencję
        self.head = (self.head + 1) % self.n
        return data