#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/24 14:40
# @Author  : jiaojianglong


a = {
    "x":2,
    "y":5,
    "z":7
}

b = {
    "x":2,
    "y":8,
    "w":4
}

print(a.keys() & b.keys())#寻找相同的key
print(a.keys() - b.keys())#寻找a中有b中没有的key
print(a.items() & b.items())#寻找相同项