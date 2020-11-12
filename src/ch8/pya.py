#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/12 10:39 上午
# @Author : FEASIN

class Student:

    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}')

    def play(self):
        print(f'{self.name}正在玩游戏')

    def __repr__(self):
        return f'{self.name}: {self.age}'


stu1 = Student('feasin', 20)

print('类的实例即对象stu1', stu1)

stu1.study('Python程序设计')