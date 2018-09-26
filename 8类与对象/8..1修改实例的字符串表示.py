#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/26 21:36
# @Author  : jiaojianglong

#可以通过定义__str__()和__repr__()方法来实现

class Pair:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s,%s)"%(self.x,self.y)

    def __repr__(self):
        return "Pair(%s,%s)"%(self.x,self.y)

p = Pair(2,5)
print(p)
print("p is {0!r}".format(p))
"""
对于__repr__(),标准的方法是让他产生的字符串文本能够满足eval(repr(x)) == x
__str__()则产生一段有意义的文本
"""
