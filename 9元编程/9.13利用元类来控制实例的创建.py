#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/12/012 19:20
# @Author  : jiaojinglong


#问题：我们想改变的创建方式，以此来实现单例模式、缓存或者其他类型的特性

#解决方案：作为python程序员，大家都应该知道如果定义了一个类，那么创建实例时就好像在调用函数一样


class Spam:

    def __init__(self,name):
        self.name = name

a = Spam("Guido")
b = Spam("Diana")

"""
如果想定制化这个步骤，则可以通过定义一个元类并以某种方式重新实现它的__call__()方法
"""

class NoInstances(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instanciate directly")


class Spam(metaclass=NoInstances):
    @staticmethod
    def grok(x):
        print("Spam.grok")


"""
在这种情况下，用户可以调用定义的静态方法，但是没法以普通的方式创建出实例
"""

#单例模式
#TODO 还不懂 元类方式实现单例
class Singleton(type):
    def __init__(self,*args,**kwargs):
        self.__instance = None
        super().__init__(*args,**kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args,**kwargs)
            return self.__instance
        else:
            return self.__instance

class Spam(metaclass=Singleton):
    def __init__(self):
        print("Creating Spam")


#创建缓存实例


import weakref

class Cached(type):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args, **kwargs):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj


class Spams(metaclass=Cached):
    def __init__(self,name):
        print("Creating Spam({!r})".format(name))
        self.name = name


a1 = Spams("111")
b1 = Spams("222")
c1 = Spams("111")
print(a1 is c1)



