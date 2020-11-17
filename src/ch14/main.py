#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/17 10:28 上午
# @Author : FEASIN

import sys
import stud

sys.path.append('/Users/chengqunzhong/Desktop/OUTKZ/PYC/python-core-50day/src/ch13')

import pyb

print('hello in main')



print('模块路径-----', sys.path)

stud.hello()
pyb.test()