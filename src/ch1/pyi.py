#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/6 4:38 下午
# @Author : FEASIN

"""
百钱百鸡
共鸡5元一只，母鸡3元一只，小鸡1元3只，用100元买一百只鸡
问公鸡 母鸡 小鸡各多少只

version 0.1
"""
# 方法一
# 有错误穷举不全
# count = 0
# for i in range(0, 100):
#     for j in range(0, i + 1):
#         count += 1
#         small = 100 - i - j
#         sum = i*5 + j*3 + small/3
#         print(f'穷举--{count}--公鸡{i}，母鸡{j}，小鸡{small}')
#         if (sum == 100):
#             print(f'公鸡{i} 母鸡{j} 小鸡{small}')


# 方法二
count = 0
for i in range(0, 21):
    for j in range(0, 34):
        count += 1
        small = 100 - i - j
        sum = i*5 + j*3 + small/3
        print(f'穷举--{count}--公鸡{i}，母鸡{j}，小鸡{small}')
        if (sum == 100):
            print(f'公鸡{i} 母鸡{j} 小鸡{small}')


# 假设公鸡的数量为x，x的取值范围是0到20
# for x in range(0, 21):
#     # 假设母鸡的数量为y，y的取值范围是0到33
#     for y in range(0, 34):
#         z = 100 - x - y
#         if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
#             print(f'公鸡: {x}只, 母鸡: {y}只, 小鸡: {z}只')

