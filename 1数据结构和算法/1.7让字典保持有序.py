#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/24 14:21
# @Author  : jiaojianglong

import collections

d = collections.OrderedDict()#普通字典的两倍，大数据不应该使用
d['foo'] = 1
d["bar"] = 2
d["spam"] = 3
d["gork"] = 4
for i in d:
    print(i)