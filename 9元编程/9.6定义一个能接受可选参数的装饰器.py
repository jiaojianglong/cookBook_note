#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/8/008 20:11
# @Author  : jiaojinglong


#问题：我们想编写一个单独的装饰器，使其既可以像@decorator 这样不带参数，也可以像@decorator(x,y,z)这样接收可选参数


#解决方案：

from functools import wraps,partial
import logging


def logged(func=None,*,level=logging.DEBUG,name=None,message=None):
    if func is None:
        return partial(logged,level=level,name=name,message=message)

    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__
    @wraps(func)
    def wrapper(*args,**kwargs):
        log.log(level,logmsg)
        return func(*args,**kwargs)
    return wrapper



@logged
def add(x,y):
    logging.debug("hahahah")
    return x+y

#没有参数时，装饰器就相当于：logged(func),所以装饰器的第一个参数就是func,其他都是可选参数

@logged(level=logging.CRITICAL,name="example")
def spam():
    print("spam!!!")

#有参数时，装饰器就相当于logged(level=logging.DEBUG,name="example")(spam)
#巧妙的利用functools.partial 将构建好的方法返回

add(1,2)
spam()


