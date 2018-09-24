#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/24 13:59
# @Author  : jiaojianglong

import heapq


#列表中实际存一个元组，（-priority,self._index,item）
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def get(self):
        return self._queue

q = PriorityQueue()
q.push("foo",2)
q.push("sdf",3)
q.push("sfasc",5)
q.push("fdsg",4)
print(q.pop())
print(q.get())