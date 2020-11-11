#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/11 6:09 下午
# @Author : FEASIN

students = {
    1001: {'name': '狄仁杰', 'sex': False, 'age': 22, 'place': '山西大同'},
    1002: {'name': '白元芳', 'sex': False, 'age': 23, 'place': '河北保定'},
    1003: {'name': '武则天', 'sex': True, 'age': 20, 'place': '四川广元'}
}

# 使用get方法通过键获取对应的值
# 如果取不到不会引发KeyError，而是返回None或者设定的默认值
print(students.get(1001))
print(students.get(1005, {'name': '无名氏'}))

# 字典中所有的键
print(students.keys())

# 字典中所有的值
print(students.values())

# 获取字典中的所有键值对
print(students.items())

# 对字典中所有的键值对进行循环遍历
for key, value in students.items():
    print(key, '---->', value)

# 使用popitem方法删除字典中最后一组键值对并返回对应对二元组
key, value = students.popitem()
print('删除后的二元组', key, value)
print('删除后的students', students.items())

# setdefault可以更新字典中的键对应的值或向字典中存入新的键值对
# 如果这个键在字典中存在，更新这键之后会返回原来与这个键对应的值
# 如果这个键在字典中不存在，方法将返回第二个参数的值，默认值是None
result = students.setdefault(1005, {'name': '方启鹤', 'sex': False})
print('返回值---', result)
print(students)

# 使用update更新字典元素，相同的键会用新的值覆盖掉旧值，不同的键会添加到字典中
others = {
    1005: {'name': '乔峰', 'sex': False, 'age': 32},
    1010: {'name': '王语嫣', 'sex': True, 'age': 19},
    1008: {'name': '钟灵', 'sex': True, 'age': 18}
}

students.update(others)
print('update 更新---', students)

