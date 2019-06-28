#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/7/007 22:05
# @Author  : jiaojinglong


#问题： 我们已经把装饰器添加到函数上了，但是想撤销它，访问未经包装的原函数。


#解决方案：假设装饰器已经实现了@warps(func)，一般来说我们可以通过访问__wrapped__属性来获取到原函数