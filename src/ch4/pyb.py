#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/10 2:03 下午
# @Author : FEASIN

items = ['Python', 'Java', 'Go', 'Kotlin']

# 使用append方法在列表尾部添加元素
items.append('Swift')
print(items)

# 使用insert方法在列表指定索引位置
items.insert(2, 'SQL')
print(items)

# 删除指定的元素
items.remove('Java')
print(items)

# 删除指定索引位置的元素
items.pop(0)
print(items)
items.pop(len(items) - 1)
print(items)

# 清空列表中的元素
items.clear()
print(items)

other = ['Python', 'Java', 'Java', 'Go', 'Kotlin', 'Python']

print(other.index('Python'))
print(other.index('Python', 1))
print(other.count('Java'))
print(other.count('Swfit'))