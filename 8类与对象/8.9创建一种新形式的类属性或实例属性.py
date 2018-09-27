#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 21:28
# @Author  : jiaojianglong


#如果想定义一种新形式的实例属性，可以以描述符的形式定义其功能。

class Integer():

    def __init__(self,name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value,int):
            raise TypeError("Expected an int")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer("x")
    y = Integer("y")

    def __init__(self,x,y):
        self.x = x
        self.y = y

p = Point(2,3)
print(p.x)#2
p.y = 5
print(p.y)#5
# p.x = "a"#TypeError: Expected an int
print(Point.x)#<__main__.Integer object at 0x00000141E2ABB5F8>

#__get__()方法看起来有些复杂的原因是实例变量和类变量的区别，如果是类变量则简单的返回描述符本身，如果是实例变量返回定义的值

#关于描述符，常容易困惑的地方就是他们只能在类的层次上定义，不能根据实例来产生，下面的代码是无法工作的

class Point:

    def __init__(self,x,y):
        self.x = Integer("x")
        self.y = Integer("y")
        self.x = x
        self.y = y

p = Point(2,"c")
print(p.x)#2
print(p.y)#c

class Typed:
    def __init__(self,name,expected_type):
        self.name = name
        self.expected_type = expected_type


    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value,self.expected_type):
            raise TypeError("Expected %s"%self.expected_type)
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

def typeassert(**kwargs):
    def decorate(cls):
        for name,expected_type in kwargs.items():
            setattr(cls,name,Typed(name,expected_type))
        return cls
    return decorate

@typeassert(name=str,shares = int,price=float)
class Stock:
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price


#对于少量的定制还是使用property简单些，如果是大量的定制则使用描述符要简单些
