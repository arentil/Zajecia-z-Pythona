#!/usr/bin/python
# -*- coding: utf-8 -*-
#kompilacja z python3

from queue import PriorityQueue

class PriorityQ(PriorityQueue):
    def __init__(self):
        PriorityQueue.__init__(self)
        self.counter = 0

    def push(self, item, priority):
        PriorityQueue.put(self, (priority, self.counter, item))
        self.counter += 1

    def pop(self, *args, **kwargs):
        _, _, item = PriorityQueue.get(self, *args, **kwargs)
        return item