#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/6 3:26 下午
# @Author : FEASIN

"""
猜数字游戏

version 0.1
"""
import random

# 产生一个1～100范围的随机数
number = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    answer = int(input('请输入：'))
    if number > answer:
        print('再大一点')
    elif number < answer:
        print('再小一点')
    else:
        print('恭喜你猜对了！')
        break
print(f'你总共猜了{counter}次')