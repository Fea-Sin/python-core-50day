#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/13 11:50 上午
# @Author : FEASIN

"""
捕获异常程序可以从异常中恢复

version 0.1
"""

class InputError(ValueError):
    """自定义异常类型"""
    pass

def fac(num):
    """求阶乘"""
    if type(num) != int or num < 0:
        raise InputError('只能计算非负整数的阶乘')
    if num in (0, 1):
        return 1
    return num * fac(num - 1)

flag = True

while flag:
    num = int(input('n = '))
    try:
        print(f'{num}! = {fac(num)}')
    except InputError as err:
        flag = False
        print(err)