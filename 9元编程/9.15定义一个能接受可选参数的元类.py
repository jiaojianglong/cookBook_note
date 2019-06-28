#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/12/012 21:00
# @Author  : jiaojinglong


#问题：我们想定义一个元类，使得在定义类的时候能够提供可选的参数，这样的话在创建类型的时候可以对处理过程惊醒控制或配置

#我们想想下面一样定义类：
#class Spam(metaclass=MyMeta,debug=True,synchronize=True):
#想要实现这样的定义方式，元类必须保证实现__prepare__(),__new__(),__init__()时使用keyword_only参数来指定他们


class MyMeta(type):
    @classmethod
    def __prepare__(metacls, name, bases,*,debug=False,synchronize=False):
        #....
        return super().__prepare__(name,bases)

    def __new__(cls,name,bases,ns,*,debug=False,synchronize=False):
        return super().__new__(cls,name,bases,ns)

    def __init__(self,name,bases,ns,*,debug=False,synchronize=False):
        super().__init__(name,bases,ns)


#创建一个类时，首先调用的是__prepare__(),这个方法一般来说只是简单的返回一个字典或其他映射型对象。
#然后调用__new__(),这个方法是用来实例化最终创建的类型对象。
#最后调用的是__init__(),用来执行其他额外的初始化步骤。


#类变量只可以被元类的__new__(),__init__(),方法访问！！！

