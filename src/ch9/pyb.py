#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/13 11:26 上午
# @Author : FEASIN

lines = ['标题：《致橡树》', '作者：舒婷', '时间：1977年3月']

file = open('onea.txt', 'a', encoding='utf-8')

for line in lines:
    file.write(f'\n{line}')

file.close()