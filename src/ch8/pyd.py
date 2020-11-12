#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/12 2:39 下午
# @Author : FEASIN

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name}正在吃饭')

    def sleep(self):
        print(f'{self.name}正在睡觉')


class Student(Person):

    def __init__(self, name, age):
        super().__init__(name, age)

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}')


class Teacher(Person):

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title

    def teach(self, course_name):
        print(f'{self.name}-{self.title}正在教授{course_name}')


stu1 = Student('元白芳', 21)
stu2 = Student('狄仁杰', 22)
teacher = Teacher('武则天', 35, '副教授')

stu1.eat()
stu2.sleep()
teacher.teach('Python程序设计')
stu1.study('Python程序设计')