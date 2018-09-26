#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/26 21:56
# @Author  : jiaojianglong

#我们想让对象通过format()函数和字符串方法来支持自定义的输出格式


#要自定义字符串的输出格式，可以在类中定义__format__()方法


_formats = {
    "ymd":"{d.year}-{d.month}-{d.day}",
    "mdy":"{d.month}/{d.day}/{d.year}",
    "dmy":"{d.day}/{d.month}/{d.year}"
}

class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self,code):
        if code == "":
            code = "ymd"
        fmt = _formats[code]
        return fmt.format(d = self)

d = Date(2018,9,26)
print(format(d))
print(format(d,"dmy"))
print(format(d,"mdy"))