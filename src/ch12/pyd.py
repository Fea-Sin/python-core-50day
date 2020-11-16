#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/16 3:40 下午
# @Author : FEASIN

import json
from collections import Counter

# 获取数据
text = ''
with open('two/movie.txt', 'r', encoding='utf-8') as file:
    for line in file:
        text += line

# 分析数据
counter = Counter(text)
top = counter.most_common(6)
# print('分析---', counter.most_common(5))
print('高频字---TOP5', top[1:])

# with open('two/data.txt', 'w', encoding='utf-8') as fileD:
#     json.dump(counter, fileD)


print('程序执行结束')

