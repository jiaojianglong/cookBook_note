#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/10 21:56
# @Author  : jiaojianglong


list_a = [1,2,3,4,5,6,7,8,9]

a,b,c,d,e,f,g,h,i = list_a

print(a,b,c,d,e,f,g,h,i)


_,b,c,d,e,f,g,h,_ = list_a #不要的数据使用一个没有用的变量接收

print(b,c,d,e,f,g,h)