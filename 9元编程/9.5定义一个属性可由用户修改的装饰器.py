#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/7/007 22:18
# @Author  : jiaojinglong

#问题：我们想编写一个装饰器来包装函数，但是可以让用户调整装饰器的属性，这样在运行时就能够控制装饰器的行为


from functools import wraps,partial
import logging

def attach_wrapper(obj,func=None):
    if func is None:
        return partial(attach_wrapper,obj)
    setattr(obj,func.__name__,func)
    return func

def logged(level,name=None,message=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args,**kwargs):
            log.log(level,logmsg)
            return func(*args,**kwargs)

        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg


        return wrapper
    return decorate

logging.basicConfig(level=logging.DEBUG)
@logged(logging.DEBUG)
def add(x,y):
    return x + y

add(2,5)

add.set_message("Add called")
add(3,8)

add.set_level(logging.WARNING)
add(2,8)


#想法：这个装饰器相当于给函数额外添加了属性，并且通过属性可以控制装饰器的执行
#相当于函数的装饰器行为在后期是可以变化的

