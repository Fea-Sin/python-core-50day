#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/13 4:52 下午
# @Author : FEASIN

import itertools


# 生成全排序
# for value in itertools.permutations('ABCD'):
#     print(value)

# 产生ABCD 和 123 的笛卡尔积
for value in itertools.product('ABCD', '123'):
    print(value)
