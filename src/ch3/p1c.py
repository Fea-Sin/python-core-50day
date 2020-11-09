#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/9 4:09 下午
# @Author : FEASIN

s1 = 'hello world'
s2 = 'hello world'
s3 = s2

#比较字符串的内容
print(s1 == s2, s2 == s3)

# 比较字符串的内存地址
print('s1 is s2===', s1 is s2, s2 is s3)

print('wo' in s1)
s4 = 'goodbye'
print(s4 in s1)