#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/7/007 22:09
# @Author  : jiaojinglong


#问题：我们想编写一个可接收参数的装饰器函数


#解决方案：假设我们想编写一个为函数添加日志功能的装饰器，但是又允许用户指定日志的等级以及一些其他的细节操作作为参数。

import logging
import functools

def logged(level,name=None,message=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            log.log(level,message)
            return func(*args,**kwargs)
        return wrapper
    return decorate