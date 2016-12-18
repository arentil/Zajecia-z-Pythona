#!/usr/bin/python
# -*- coding: utf-8 -*-
#kompilacja z python3

#zadanie 10.2 (stack) implementacja tablicowa

class Stack:

    def __init__(self, size=10):
        self.items = size * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementów na stosie
        self.size = size                # maksymalny rozmiar stosu

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):       # ma zgłaszać błąd w przypadku przepełnienia stosu
        if (self.n == self.size):
            raise Exception("Stack full!")
        self.items[self.n] = data
        self.n = self.n + 1

    def pop(self):              # ma zgłaszać błąd w przypadku pustego stosu
        if (self.n == 0):
            raise Exception("Stack empty!")
        self.n = self.n - 1
        data = self.items[self.n]
        self.items[self.n] = None    # usuwam referencję
        return data