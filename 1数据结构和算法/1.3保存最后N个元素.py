#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/24 13:26
# @Author  : jiaojianglong

import collections



def search(lines,pattern,history = 5):
    previous_lines = collections.deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line,previous_lines
        previous_lines.append(line)

if __name__ =="__main__":
    with open("test.txt","r",encoding="utf8") as f:
        for line,previous in search(f,"python",5):
            for pline in previous:
                print(pline,end="")
            print(line,end="")
            print("-"*20)









#collections.deque使用简介
queue = collections.deque(["jiao","li",'hao',"yu"])
queue.appendleft("wu")
print(queue)
queue.append("haha")
print(queue)
queue.popleft()
print(queue)