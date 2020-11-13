#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/13 3:38 下午
# @Author : FEASIN

from collections import Counter

words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
         'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
         'look', 'into', 'my', 'eyes', "you're", 'under']

counter = Counter(words)

for elem, count in counter.most_common():
    print(f'计数---{elem}---{count}')