#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/11 6:41 下午
# @Author : FEASIN

sentence = input('请输入一段话：')
counter = {}

for ch in sentence:
    if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
        counter[ch] = counter.get(ch, 0) + 1

for key, value in counter.items():
    print(f'字母{key} --- 出现了 --> {value} 次')