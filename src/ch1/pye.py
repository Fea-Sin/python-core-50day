#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/6 3:20 下午
# @Author : FEASIN

"""
打印乘法口诀表

version 0.1
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}*{j} = {i * j}', end='\t')
    print()

