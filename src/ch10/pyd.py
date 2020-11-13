#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/13 4:44 下午
# @Author : FEASIN

import heapq

list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

# 价格最高的2只股票
print(heapq.nlargest(2, list2, key=lambda x: x['price']))

# 找出持有数量最高的2只股票
print(heapq.nlargest(2, list2, key=lambda x: x['shares']))