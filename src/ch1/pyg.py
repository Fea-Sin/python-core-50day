#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/6 4:22 下午
# @Author : FEASIN

"""
寻找所有水仙花

version 0.1
"""
for num in range(100, 1000):
    low = num % 10
    mid = (num // 10) % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)