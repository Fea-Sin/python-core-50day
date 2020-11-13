#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/13 4:33 下午
# @Author : FEASIN

import hashlib

# 计算字符串的MD5摘要
print(hashlib.md5('123456'.encode()).hexdigest())

# 计算文件的MD5摘要
hasher = hashlib.md5()

with open('The-C-Programming-Language.pdf', 'rb') as file:
    data = file.read(512)
    while data:
        hasher.update(data)
        data = file.read()

print('文件指纹---', hasher.hexdigest())

