#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/9 4:15 下午
# @Author : FEASIN

s = 'abc123456'

N = len(s)
print(f'N-->{N}')

"""索引"""

# 获取第一个字符
print(s[0], s[-N])

# 获取最后一个字符
print(s[N-1], s[-1])

# 获取索引为2或-7的字符
print(s[2], s[-7])

"""切片"""

# i=2 j=5 k=1 正向切片
print(s[2:5])

# i=-7 j=-4 k=1 正向切片
print(s[-7:-4])

# i=2 j=9 k=1 正向切片
print(s[2:])

# i=-7 j=-1 k=1 正向切片
print(s[-7:])

# i=2 j=9 k=2 正向切片
print(s[2::2])

# i=0 j=9 k=2 正向切片
print(s[::2])

# i=7 j=1 k=2 负向切片
# 输出为反向顺序
# ==> 54321c
print('负向切片', s[7:1:-1])

# i=-1 j=-9 k=-1 负向切片
print(s[::-1])

# i=-1 j=-9 k=-2 负向切片
print(s[::-2])
