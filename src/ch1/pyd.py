#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/6 3:13 下午
# @Author :

"""
用for循环实现1～100求和

version 0.1
"""

total = 0
for x in range(1, 101):
    total += x
print(f'1~100求和结果：{total}')