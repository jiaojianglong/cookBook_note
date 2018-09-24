#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/24 13:10
# @Author  : jiaojianglong


list_a = range(2)
first,*middle,last = list_a#使用*来接收任意数量，甚至没有，返回一个list
print(first,middle,last)


records = [
    ("foo",1,2),
    ("bar","hello"),
    ("foo",3,4)
]

def do_foo(x,y):
    print("foo",x,y)

def do_bar(s):
    print("bar",s)

for tags,*args in records:
    if tags == "foo":
        do_foo(*args)
    elif tags == "bar":
        do_bar(*args)