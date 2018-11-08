#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/8/008 21:54
# @Author  : jiaojinglong


#问题：我们想编写一个装饰器，为被包装的函数添加额外的参数，但是添加的参数不能影响到该函数已有的调用约定


#解决方案：
from functools import wraps

def optinoal_debug(func):
    @wraps(func)
    def wrapper(*args,debug=False,**kwargs):
        if debug:
            print("Calling",func.__name__)
        return func(*args,**kwargs)
    return wrapper

#函数中的一部分参数被装饰器解析所用，剩下参数给到函数，可以用被包装函数的参数来控制装饰器的行为
