#!/usr/bin/python
# -*- coding: utf-8 -*-
#kompilacja z python3

#zadanie 10.8

from random import randint

class RandomQueue:

    def __init__(self, size = 10):
        self.n = size
        self.items = self.n * [None]          # tablica elementów
        self.iFull = []                       # lista indeksów zajętych w tablicy "items"
        self.iEmpty = list(range(0, size))    # lista indeksów pustych w tablicy "items"

    def insert(self, item):
        if (self.is_full()):
            raise Exception("RandomQueue full!")
        i = self.iEmpty.pop()
        self.items[i] = item
        self.iFull.append(i)

    def remove(self):   # zwraca losowy element
        if (self.is_empty()):
            raise Exception("RandomQueue empty!")
        i = self.iFull.pop(randint(0, len(self.iFull)-1))
        item = self.items[i]
        self.items[i] = None
        return item

    def is_empty(self):
        return (len(self.iFull) == 0)

    def is_full(self):
        return (len(self.iEmpty) == 0)


'''
    Na dowód, że ta implementacja działa, włożę do kolejki po kolei liczby od 1 do 10,
    następnie wypisuję na ekran kolejne usuniete elementy z kolejki. Kolejność liczb
    wypisanych na ekran powinna być za każdym razem inna(prawdopodobieństwo wyrzucenia
    na ekran tych samych danych jest wysoce nieprawdopodobne, ale możliwe)
'''

rq = RandomQueue()
rq.insert(1)
rq.insert(2)
rq.insert(3)
rq.insert(4)
rq.insert(5)
rq.insert(6)
rq.insert(7)
rq.insert(8)
rq.insert(9)
rq.insert(10)
while not rq.is_empty():
    print(rq.remove())
