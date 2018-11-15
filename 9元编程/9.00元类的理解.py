#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/13/013 20:34
# @Author  : jiaojinglong

#
# class A():
#     def __init__(self,name):
#         self.name = name
#         print("创建了一个实例")

# a = type("a",(A,),{"name":"jiao"})
# print(a)
# print(a.name)
# print(a("jiang"))


class UpperAttrMetaClass(type):
    def __new__(cls,class_name,class_parents,class_attr, *args, **kwargs):
        print("__new__")
        class_attr['name'] = "jiao"
        res  = type.__new__(cls,class_name,class_parents,class_attr)
        print(res)
        return res

    def __init__(self,*args,**kwargs):
        print("__init__")
        super().__init__(*args, **kwargs)
        self.__cache = {}

    def __call__(self, *args, **kwargs):
        print("__call__")
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            print(obj)
            return obj


class A(metaclass=UpperAttrMetaClass):
    def __init__(self,name):
        self.name = name
        print("a.__init__")

a = A("jiao")
# b = A("jiao")
# c = A("jiang")
# print(a.name)
