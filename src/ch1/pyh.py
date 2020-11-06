#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/6 4:31 下午
# @Author : FEASIN

"""
正整数反转

version 0.1
"""
num = int(input('输入数据：'))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(f'反转后的数字：{reversed_num}')