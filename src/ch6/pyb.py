#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/11 4:16 下午
# @Author : FEASIN

set1 = {'Python', 'Java', 'Go', 'Swift'}
print('Java' in set1)
print('Ruby' in set1)

set2 = {1, 2, 3, 4, 5, 6, 7}
set3 = {2, 4, 6, 8, 10}

# 交集
print(set2 & set3)

# 并集
print(set2 | set3)

# 差集
print(set2 - set3)

# 对称差
print(set2 ^ set3)

set4 = {1, 3, 5}
set5 = {1, 2, 3, 4, 5}

# 真子集
print(set4 < set5)

# 超集
print(set5 > set4)