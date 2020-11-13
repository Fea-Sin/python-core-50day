#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/13 2:00 下午
# @Author : FEASIN

try:
    with open('img/dog.jpeg', 'rb') as file1:
        data = file1.read()
        print('图片二进制数据----', data)
    with open('img/he.jpeg', 'wb') as file2:
        file2.write(data)
except FileNotFoundError:
    print('指定文件无法打开')
except IOError:
    print('读写文件时出错')

print('程序执行结束')