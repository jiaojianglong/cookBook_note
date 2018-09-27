#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 20:22
# @Author  : jiaojianglong

#“私有属性的封装”


#在python中，以单下划线_开头的属性被认为是一种私有属性

class A:
    def __init__(self):
        self._name = "jiaojianglong"
        self.age = 24

    def _internal_method(self):
        print("i am a internal method")


a = A()
print(a._name) #jiaojianglong

#python并不会阻止访问属性，但编译器不会做提示。如果强行访问会被认为是粗鲁的。


#在类的定义中也见到过双下划线__开头的名称，以双下划线开头的名称会导致出现名称重组的行为，

class B:
    def __init__(self):
        self.__name = "jiaojianglong"

b = B()
# print(b.__name)#AttributeError: 'B' object has no attribute '__name'
print(b._B__name)#jiaojianglong

#这样的行为是为了继承，以双下划线开头的属性不会被子类通过继承而覆盖。

class C(B):
    def __init__(self):
        super().__init__()

c = C()
print(c._B__name)#jiaojianglong

#大部分情况下我们使用单下划线，涉及到子类继承覆盖的问题时使用双下划线
#当我们想定义一个变量，但是名称可能会与保留字段冲突，基于此，我们在名称后加一个单下划线以示区别。lambda_