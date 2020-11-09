#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/9 1:56 下午
# @Author : FEASIN

"""
参数默认值

version 0.1
"""
from random import randint

def roll_dice(n=2):
    """摇骰子返回总点数"""
    total = 0
    for _ in range(n):
        total += randint(1, 6)

    return total

# 如果没有指定参数，那么n使用默认值2，表示摇两颗骰子
print(roll_dice())

# 如果传入参数3，n被赋予值为3，表示摇3科骰子
print(roll_dice(3))