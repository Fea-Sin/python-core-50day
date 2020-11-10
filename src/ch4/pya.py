#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/10 11:50 上午
# @Author : FEASIN

"""
将一颗骰子掷6000次，统计每个点数出现次数

version 0.1
"""

import random

counters = [0] * 6

for _ in range(60000000):
    face = random.randint(1, 6)
    counters[face -1] += 1

for face in range(1, 7):
    print(f'{face}点出现了{counters[face - 1]}次')
