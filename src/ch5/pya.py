#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/10 2:57 下午
# @Author : FEASIN

t1 = (30, 10, 55)

t2 = ('feasin', 40, True, '成都')

# 拼接
t3 = t1 + t2
print('拼接', t3)

# 打包
a = 1, 10, 100
print('打包', type(a), a)

# 解包
i, j, k = a
print('解包', i, j, k)

b = 1, 10, 100, 1000
i, j, *k = b
print('星号表达式', i, j, k)
i, *j, k = b
print('星号表达式', i, j, k)
*i, j, k = b
print('星号表达式', i, j, k)

# 简洁的赋值
a, b, *c = range(1, 10)
print('range 赋值', a, b, c)

a, *b , c = 'hello'
print('赋值', a, b, c)