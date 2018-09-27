#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 20:06
# @Author  : jiaojianglong

#当我们的程序需要创建大量的实例（百万级），这样会占用大量的内存。

#对于那些主要用作简单数据结构的类，通常可以在类定义中增加__slot__属性，以此来大量减少对内存的使用。

class Date:
    __slots__ = ["year","month","day"]

    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day


#当定义了__slots__属性时，python会采用一种更加紧凑的内部表示，会将实例的属性添加到一个小型数组里，不再为每个实例创建__dict__。
#副作用是我们不能为实例添加新的属性。是一种优化手段

