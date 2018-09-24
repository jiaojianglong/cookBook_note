#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/24 14:27
# @Author  : jiaojianglong

#字典进行大小运算时都是使用key值进行大小比较，而我们一般想要用value值比较，而且还想要得到该值的key

prices = {
    "ACME":23,
    "AAPL":345,
    "IBM":34,
    "FB":24
}

#利用zip,zip返回一个迭代器，只能使用一次

min_price = min(zip(prices.values(),prices.keys()))
print(min_price)

#排序
price_sorted = sorted(zip(prices.values(),prices.keys()))
print(price_sorted)

