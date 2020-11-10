#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/10 2:21 下午
# @Author : FEASIN

"""
字符串笛卡尔积

version
"""

item = []
for x in 'ABCDE':
    for y in '123':
        item.append(x + y)

print('笛卡尔积', item)
print('笛卡尔积元素个数', len(item))