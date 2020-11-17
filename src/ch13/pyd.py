#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/17 2:03 下午
# @Author : FEASIN

import pya

soup = pya.get_movie()

"""获取所有文本"""

print('输出文本'.center(50, '*'))
for string in soup.stripped_strings:
    print(str(string))