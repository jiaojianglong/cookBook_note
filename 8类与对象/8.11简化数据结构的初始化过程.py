#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/18/018 14:54
# @Author  : jiaojinglong


# 问题：我们编写了许多类，把他们当作数据结构来用，但是我们厌倦了编写高度重复代码且样式相同的__init__()。

# 解决方案：通常我们可以将初始化数据结构的步骤归纳到__init__()函数中，并将其定义在一个公共的基类中。


class Structurs():
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError("Expected {} arguments".format(len(self._fields)))

        for name, value in zip(self._fields, args):
            setattr(self, name, value)


# example:
class Point(Structurs):
    _fields = ["x", "y"]

# 对关键字参数的支持