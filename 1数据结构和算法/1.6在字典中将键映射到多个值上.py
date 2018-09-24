#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/24 14:15
# @Author  : jiaojianglong

import collections

d = collections.defaultdict(list)#自动初始化，不用判断是否存在
d["a"].append(1)
d["a"].append(1)
d["a"].append(1)
d["a"].append(1)
print(d['a'])