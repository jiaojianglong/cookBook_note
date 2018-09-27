#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 20:59
# @Author  : jiaojianglong

#我们想调用一个父类中的方法，这个方法在子类中已经被覆盖了。


class A:
    def spam(self):
        print("A.spam")

class B(A):
    def spam(self):
        print("B.spam")
        super().spam()

b = B().spam()#B.spam,A.spam

#争对每一个类，python都会计算出一个称为方法解析顺序（MRO）的列表，MOR列表只是简单的对所有的基类进行线性排列。
print(B.__mro__)#(<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
