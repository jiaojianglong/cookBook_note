#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/12/012 20:19
# @Author  : jiaojinglong


#问题：我们想自动记录下属性和方法在类中的定义顺序，这样就能利用这个顺序来完成各种操作你（序列化处理，将属性映射到数据库）

#解决方案：

from collections import OrderedDict

class Typed:
    _excepted_type = type(None)

    def __init__(self,name=None):
        self._name = name

    def __set__(self, instance, value):
        if not isinstance(value,self._excepted_type):
            raise TypeError("Excepted"+str(self._excepted_type))
        instance.__dict__[self._name] = value

class Integer(Typed):
    _excepted_type = int

class Float(Typed):
    _excepted_type = float

class String(Typed):
    _excepted_type = str

class OrderedMeta(type):

    def __new__(cls, clsname,bases,clsdict):
        d = dict(clsdict)
        order = []
        for name,value in clsdict.items():
            if isinstance(value,Typed):
                value._name = name
                order.append(name)
                d['_order'] = order
                return type.__new__(cls,clsname,bases,d)

    @classmethod
    def __prepare__(metacls, name, bases):
        return OrderedDict()

#注：__prepare__该方法会在类定义一开始的时候调用，调用时以类名和基类名称作为参数，它必须返回一个映射对象，供处理类定义体时调用


#eg.
class Structure(metaclass=OrderedMeta):

    def as_csv(self):
        return ','.join(str(getattr(self,name)) for name in self._order)

class Stock(metaclass=OrderedMeta):
    name = String()
    shares = Integer()
    price = Float()
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price

s = Stock("haha",23,23.3)
print(s.name)
s = Stock(34,23,34)
# print(s.as_csv())
