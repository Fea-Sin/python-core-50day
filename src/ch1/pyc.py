#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/6 2:36 下午
# @Author : FEASIN

"""
分段函数求值

version 0.1
"""

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3

print(f'f({x}) = {y}')