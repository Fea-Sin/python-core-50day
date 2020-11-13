#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/13 11:05 上午
# @Author : FEASIN

import sys
import time

# 当前系统默认的编码
# print(sys.getdefaultencoding())

file = open('致橡树.txt')

for line in file:
    print(line, end='')
    time.sleep(0.5)

file.close()