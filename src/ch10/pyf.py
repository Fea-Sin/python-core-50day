#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/13 5:15 下午
# @Author : FEASIN

from os import path
import uuid

# 返回目录
print('返回目录', path.dirname('hello/ch10/pyf.py'))

# 文件存在判断
print('文件存在判断', path.exists('./pyf.py'))

# 文件最后访问时间、修改时间、创建时间
print('最后访问时间---', path.getatime('pya.py'))
print('修改时间---', path.getmtime('pya.py'))
print('创建时间---', path.getctime('pya.py'))

# 文件大小
print('文件大小', path.getsize('The-C-Programming-Language.pdf'))

# 连接路径
print('连接路径', path.join('python-core-50day', 'src', 'ch10', ''))

#
print('路径---', path.splitext('src/ch10/The-C-Programming-Language.pdf'))

print('全球唯一性', uuid.uuid1().hex)