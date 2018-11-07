#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/7/007 21:52
# @Author  : jiaojinglong


#问题：当一个函数被装饰器装饰时，一些重要的元数据比如：函数名、文档字符串、函数注解以及调用签名都丢失了



#解决方案：每当定义一个装饰器时应该总是记得为底层的包装函数添加functools库中的@wraps装饰器

import time
import functools
def timethis(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        print(func.__name__,end_time-start_time)
        return result
    return wrapper

@timethis
def mysleep(num:int):
    """
    原函数注释文档
    :param num:
    :return:
    """
    time.sleep(num)
    print("我是原函数")


mysleep(3)
print(mysleep.__name__)
print(mysleep.__doc__)
print(mysleep.__annotations__)


#如果装饰器使用@functools.wraps(func) 装饰，我们就可以使用下面的方法获取到原函数！！！
mysleep.__wrapped__(3)