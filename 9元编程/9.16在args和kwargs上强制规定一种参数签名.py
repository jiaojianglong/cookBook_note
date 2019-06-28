#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/15/015 21:02
# @Author  : jiaojinglong


#问题：我们已经编写了一个使用*args和**kwargs作为参数的函数或方法，这样使得函数或方法成为通用型的，但是我们也想对传入参数做检查，
#看看他们是否匹配了某个特定的函数调用签名

#解决方案：使用inspect模块


from inspect import Signature,Parameter


parms = [Parameter("x",Parameter.POSITIONAL_OR_KEYWORD),
         Parameter("y",Parameter.POSITIONAL_OR_KEYWORD,default=42),
         Parameter("z",Parameter.KEYWORD_ONLY,default=None)
         ]

sig = Signature(parms)
print(sig)

#一旦有了签名对象，就可以通过对象的bind()方法轻松将其绑定到*args,**kwargs上

def func(*args,**kwargs):
    bound_values = sig.bind(*args,**kwargs)
    for name,value in bound_values.arguments.items():
        print(name,value)


func(1,2)

#一个更加具体的例子：

def make_sig(*names):
    parms = [
        Parameter(name,Parameter.POSITIONAL_OR_KEYWORD) for name in names
    ]
    return Signature(parms)

class Structure:
    __signature__ = make_sig()

    def __init__(self,*args,**kwargs):
        bound_value = self.__signature__.bind(*args,**kwargs)
        for name,value in bound_value.arguments.items():
            setattr(self,name,value)


class Point(Structure):
    __signature__ = make_sig("name","shares","price")


class Stock(Structure):
    __signature__ = make_sig("x","y")


#使用示例：
p1 = Point(1,2,3)


#也可以使用元类来实现此过程

def make_sig(*names):
    parms = [Parameter(name,Parameter.POSITIONAL_OR_KEYWORD) for name in names]
    return Signature(parms)

class StructureMeta(type):
    def __new__(cls, clsname,bases,clsdict):
        clsdict['__signature__'] = make_sig(clsdict.get("_fields",[]))
        return super().__new__(cls,clsname,bases,clsdict)

class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self,*args,**kwargs):
        bound_values = self.__signature__.bind(*args,**kwargs)
        for name,value in bound_values.arguments.items():
            setattr(self,name,value)

class Point(Structure):
    _fields = ["x","y"]