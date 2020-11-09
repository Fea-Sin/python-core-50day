#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/9 11:58 上午
# @Author : FEASIN

"""
输入M和N计算C(M, N)

version 0.1
"""

# 定义函数：def是定义函数的关键字、fac是函数名，num是参数

def fac(num):
    """求阶乘"""
    res = 1
    for n in range(1, num + 1):
        res *= n

    return res

# 计算 C(M, N)
m = int(input('m = '))
n = int(input('n = '))

print(fac(m) // fac(n) // fac(m-n))