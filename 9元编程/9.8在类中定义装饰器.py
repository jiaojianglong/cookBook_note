#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/8/008 21:20
# @Author  : jiaojinglong


#问题： 我们想在类中定义一个装饰器，并将其作用到其他函数或方法上

#解决方案：

from functools import wraps

class A:
    def decorator1(self,func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print("decorator 1")
            return func(*args,**kwargs)
        return wrapper

    @classmethod
    def decorator2(cls,func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print("decorator 2")
            return func(*args,**kwargs)
        return wrapper


#思考：@property 实际上是一个拥有 getter(),setter(),deleter()方法的类，每一个方法都可作为一个装饰器
#几个装饰器都可以操纵实例的状态，因此，如果需要装饰器在背后记录或合并信息，这是一个很明智的方法。