#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/18/018 16:08
# @Author  : jiaojinglong

#问题：我们正在编写一个类，但是想让用户能够以多种方式创建实例，而不局限于__init__()提供的这一种

#解决方案：要定义一个含有多个构造函数的类，应该使用类方法

import time
class Date():
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year,t.tm_month,t.tm_day)

a = Date(2012,12,12)
b = Date.today()