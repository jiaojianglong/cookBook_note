#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/24 14:47
# @Author  : jiaojianglong

def dedupe(items,key = None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)