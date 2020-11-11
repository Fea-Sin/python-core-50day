#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/11 4:07 下午
# @Author : FEASIN

set1 = {1, 2, 3, 3, 2}
print(set1)

set2 = set('hello')
print(set2)

set3 = set([1, 2, 3, 3, 1])
print(set3)

set4 = {num for num in range(1, 40) if num % 3 == 0 or num % 5 == 0}

print(set4)

# 集合元素循环遍历
for elem in set4:
    print(elem)