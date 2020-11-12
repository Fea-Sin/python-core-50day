#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/12 2:10 下午
# @Author : FEASIN

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student('王小二', 20)
print('初始对象', stu)

stu.sex = '男'
print('添加属性', stu)

# 查看属性
print('查看属性', stu.name)
print('查看属性', stu.age)
print('查看属性', stu.sex)