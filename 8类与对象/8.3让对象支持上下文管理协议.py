#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/26 22:06
# @Author  : jiaojianglong


#我们想让对象支持上下文管理协议，即可以通过with语句触发。

#想让对象支持上下文管理协议，对象需实现__enter__()和__exit__()方法，比如实现网络连接的类。

from socket import socket,AF_INET,SOCK_STREAM
from functools import partial

class LazyConnection:

    def __init__(self,address,family = AF_INET, type = SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError("Already connected")
        self.sock = socket(self.family,self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        self.sock = None

conn = LazyConnection("www.baidu.com")

with conn as s:
    s.send(b'hahhahah')

