#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/8/008 21:45
# @Author  : jiaojinglong


#问题：我们想在类或者静态方法上应用装饰器


#解决方案：将装饰器作用到类和静态方法上是简单而直接的，但是要保证装饰器在应用的时候需要放在@classmethod 和 @staticmethod 之前，示例如下：

import time
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        r = func(*args,**kwargs)
        end = time.time()
        print(end-start)
        return r
    return wrapper

#思考：@classmethod 和 @staticmethod 装饰器并不会返回一个可执行对象，所以装饰器都要放在他们下面！！！