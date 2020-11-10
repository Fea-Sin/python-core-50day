#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/10 4:03 下午
# @Author : FEASIN

def find_max_min(items):
    """
    找到列表中最大值和最小值
    :param items:
    :return: 最大值和最小值构成的元组
    """
    max, min = items[0], items[0]
    for item in items:
        if item > max:
            max = item
        elif item < min:
            min = item

    return max, min

# test
a = [1, 34, 56, 56, 90, 3444, 8]

print(find_max_min(a))
