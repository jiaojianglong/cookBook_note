#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 20:45
# @Author  : jiaojianglong


#在对实例的获取和设定上，我们希望增加一些额外的处理过程。

class Person:
    def __init__(self,first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self,value):
        if not isinstance(value,str):
            raise TypeError("Excepted a string")
        self._first_name = value



p = Person("jiao")
#在创建实例时，__inti__（）中我们将name赋值到self.first_name,实际会调用setter方法，所以name实际还是储存在self._first_name中
print(p.first_name)
