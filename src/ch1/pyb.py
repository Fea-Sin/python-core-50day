#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/6 12:02 下午
# @Author : FEASIN

"""
将华氏温度转换为摄氏温度

version 0.1
"""

# 函数中 `%.1f` 是一个占位符，表示保留一位小数的浮点数
# 同理 `%d` 表示一个 int 类型的变量，`%s` 表示一个字符串变量

f = float(input('请输入华氏温度'))
c = (f - 32) / 1.8

print('%.1f华氏度 = %.1f摄氏度' % (f, c))