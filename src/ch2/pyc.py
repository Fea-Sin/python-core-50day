#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/9 2:07 下午
# @Author : FEASIN

"""
可变参数

version 0.1
"""

# 用星号表达式来表示args接收0个或任意多个参数
def add(*args):
    total = 0
    for val in args:
        total += val

    return total

print(add())
print(add(1, 2))
print(add(1, 3, 5, 7, 9))