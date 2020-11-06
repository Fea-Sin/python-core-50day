#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/6 11:28 上午
# @Author : FEASIN

"""
使用type()检查变量的类型
python中的类型转换操作

version 0.1
"""

a = 100
b = 12.345
c = 'hello world'
d = True

# type() 检查类型
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# 整数转换成浮点数
print(float(a))

# 浮点数转换成字符串
print(str(b))

# 字符串转换成布尔型
print(bool(c))

# 布尔型转换成整数
print(int(d))

# 将整数转换成对应字符
print(chr(97))

# 将字符转换成整数
print(ord('a'))
