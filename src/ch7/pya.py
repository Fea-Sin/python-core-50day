#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/11 5:17 下午
# @Author : FEASIN

person = {
    'name': '王大锤',
    'age': 55,
    'weight': 60,
    'office': '华科北路62号',
    'home': '中同仁路8号',
    'tel': '13100008888',
    'econtact': '13800008888'
}

print(person)
print('键值对数', len(person))
for key in person:
    print(f'{key}: {person[key]}')

item1 = dict(zip('ABCDE', '12345'))
print(item1)

# 用字典生成语法创建字典
item2 = {x: x ** 3 for x in range(1, 10)}
print(item2)