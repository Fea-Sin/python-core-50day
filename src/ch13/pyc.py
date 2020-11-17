#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/17 11:45 上午
# @Author : FEASIN

import pya

soup = pya.get_movie()

# css搜索 方式一
# for tag in soup.find_all('div', class_='billboard-bd'):
#     print('elem---', tag)

# css搜索 方式二
for tag in soup.find_all('div', attrs={'class': 'billboard-bd'}):
    # print('elem元素----', tag)
    for a in tag.find_all('a'):
        print('子元素获取---', a)

