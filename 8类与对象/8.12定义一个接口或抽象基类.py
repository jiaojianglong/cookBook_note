#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/18/018 14:54
# @Author  : jiaojinglong


#问题：我们想定义一个类作为接口或抽象基类，这样可以在此之上执行类型检查并确保在子类中实现特定的方法。

#解决方案：要定义一个抽象基类，可以使用abc模块：

from abc import ABCMeta,abstractmethod


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self,maxbytes=-1):
        pass

    @abstractmethod
    def write(self,data):
        pass


#抽象基类的核心特征就是不能被直接实例化，是用来给其他累当作基类使用的，这些子类需要实现基类中要求的那些方法。
#主要用途就是强制规定所需的编程接口