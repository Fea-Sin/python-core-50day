#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/10 11:24 上午
# @Author : FEASIN

def get_suffix(filename):
    """
    获取文件名的后缀名
    :param filename:
    :return: 文件后缀名
    """
    pos = filename.rfind('.')
    return filename[pos + 1:] if pos > 0 else ''

# test
print(get_suffix('readme.txt'))
print(get_suffix('readme.txt.md'))
print('1->', get_suffix('.gitignore'))
print('2->', get_suffix('readme.'))
print('3->', get_suffix( 'readme'))