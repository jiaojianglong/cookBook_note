#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/18/018 15:39
# @Author  : jiaojinglong


#问题：我们想实现一个自定义的类，用来模仿普通的内建容器类型比如列表或者字典的行为，但是我们并不需要实现什么方法来完成

#解决方案：collections库中定义了各种各样的抽象基类，当实现自定义的容器时他们会非常有用。

import collections
from collections import Iterable,Sequence,MutableSequence,Mapping,MutableMapping,Set,MutableSet

class A(collections.Iterable):
    pass

#可以确保实现所有必要的方法否则就会报错

#实现一个自动排序的队列

import collections
import bisect

class SortedItems(collections.Sequence):
    def __init__(self,initial=None):
        self._items = sorted(initial) if initial is not None else []


    def __getitem__(self, item):
        return self._items[item]

    def __len__(self):
        return len(self._items)

    def add(self,item):
        bisect.insort(self._items,item)