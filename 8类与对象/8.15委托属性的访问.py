#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/18/018 15:51
# @Author  : jiaojinglong

#问题：我们想在访问实例属性时能够将其委托到一个内部持有的对象上，这可以作为继承的替代方案或者是为了实现一种代理机制。

#解决方案：简单来说委托是一种编程模式，我们将某个特定的操作转交给（委托）另一个不同的对象来实现，通常来说，最简单的委托形式是这样的：

class A():

    def spam(self,x):
        pass

    def foo(self):
        pass

class B():
    def __init__(self):
        self._a = A()

    def spam(self,x):
        return self._a.spam(x)

    def foo(self):
        return self._a.foo()

    def bar(self):
        pass



#如果简单的几个方法需要委托，想上面的写法是可以的，但是如果有大量的方法需要委托，我们可以像下面一样来实现：


class B():
    def __init__(self):
        self._a = A()

    def __getattr__(self, item):#如果代码中尝试访问一个并不存在的属性就会调用这个方法
        return getattr(self._a,item)


#实现代理

class Proxy():
    def __init__(self,obj):
        self._obj = obj

    def __getattr__(self, item):
        return getattr(self._obj,item)

    def __setattr__(self, key, value):
        if key.startswith("_"):
            super().__setattr__(key,value)

        else:
            setattr(self._obj,key,value)


    def __delattr__(self, item):
        if item.startswith("_"):
            super().__delattr__(item)
        else:
            delattr(self._obj,item)

#要使用这个代理类，只需要简单地用它包装另一个实例即可：
class Spam():
    def __init__(self,x):
        self.x = x


