#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/9 5:45 下午
# @Author : FEASIN

"""
字符串性质判断
startswith, endswith

version 0.1
"""

s = 'hello world!'

print(s.startswith('hel'))

print(s.endswith('d!'))

"""数字格式化"""

n = 3.1415926

print('排的值是 {:.2f}'.format(n))

print('科学计数法 {:.2e}'.format(12345678))

print('分隔符 {:,}'.format(123456789))


