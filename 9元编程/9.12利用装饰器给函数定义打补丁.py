#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/8/008 22:02
# @Author  : jiaojinglong

#问题：我们想检查或改写一部分类的定义，以此来修改类的行为，但是不想通过继承或者元类的方式来做

#解决方案：

def log_getattribute(cls):
    orig_getattribute = cls.__getattribute__


    def new_getattribute(self,name):
        print("getting",name)
        return orig_getattribute(self,name)

    cls.__getattribute__ = new_getattribute
    return cls

@log_getattribute
class A:
    def __init__(self,x):
        self.x = x

    def spam(self):
        pass

a = A(42)
a.x



#可以通过此方法对类的属性做监控