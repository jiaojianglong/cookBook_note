#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/8/008 21:32
# @Author  : jiaojinglong


#问题： 我们想用装饰器来包装函数，但是希望得到的结果是一个可调用的实例。我们需要装饰器既能在类中工作，也可以在类外部使用


#解决方案：要把装饰器定义成类实例，需要确保在类中实现__call__()和__get__()方法

import types
from functools import wraps

class Profield:
    def __init__(self,func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls +=1
        return self.__wrapped__(*args,**kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self,instance)


#该装饰器相当于为函数添加一个属性 ncalls
