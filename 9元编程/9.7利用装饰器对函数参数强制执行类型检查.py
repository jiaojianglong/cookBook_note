#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/8/008 20:37
# @Author  : jiaojinglong

#问题：我们想为函数参数添加强制类型检查功能，将其作为一种断言或者与调用者之间的契约


from inspect import signature
from functools import wraps

def typeassert(*ty_args,**ty_kwargs):

    def decorate(func):
        if not __debug__:
            return func
        sig = signature(func)#获取func的参数签名（x,y,z）
        bound_types = sig.bind_partial(*ty_args,**ty_kwargs).arguments# 参数签名与类型参数做映射   [("x",<class "int">),("z",<class "int">)]
        @wraps(func)
        def wrapper(*args,**kwargs):
            bound_values = sig.bind(*args,**kwargs).arguments# 参数签名与函数参数做映射
            for name,value in bound_values.items():
                if name in bound_types:#判断参数是否有类型限制
                    if not isinstance(value,bound_types[name]):
                        raise TypeError("Argument {} must be {}".format(name,bound_types[name]))
            return func(*args,**kwargs)
        return wrapper
    return decorate



class A():
    def a(self):
        print("a")

@typeassert(int,A,z=int)
def add(x,y,z):
    print(x,y,z)
    return x

add(1,A(),3)


#想法：参数类型的限制可以使用在参数处理方法中，对前端接收的参数进行检查，也可以使用在一些需要限制传入参数类型的地方


#注：此装饰器一个微妙的地方，只检查传递的参数，如果是默认参数，没有进行传递，参数类型不进行检查


@typeassert(int,list)
def bar(x,items=None):
    if items is None:
        items = []
    items.append(x)
    return items

print(bar(2))