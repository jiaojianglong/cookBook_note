#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/24 13:47
# @Author  : jiaojianglong


import heapq

nums = [5,56,7,6,34,2,5,7,6,89,80,-90,0,9,-67,5,45,]

print(min(nums))
print(max(nums))

print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))

#可支持更加复杂的数据结构

portfolio = [
    {"name":"jiao","age":24},
    {"name":"jsdfo","age":2},
    {"name":"jisd","age":12},
    {"name":"jdo","age":36},
    {"name":"li","age":25},
    {"name":"jgd","age":50},
]

print(heapq.nlargest(3,portfolio,key=lambda s:s['age']))
print(max(portfolio,key=lambda s:s['age']))