#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/11 2:56 下午
# @Author : FEASIN

"""
双色球属乐透型彩票范畴，红球号码范围01-33，蓝球号码范围01-16
双色球每期从33个红球中开出6个号码，从16个蓝球中开出1个号码

version 0.1
"""
from random import randint, sample

def display(bills):
    """
    输出列表中的双色球号码
    :param bills:
    :return:
    """
    for index, ball in enumerate(bills):
        if index == len(bills) - 1:
            print('|', end=' ')
        print(f'{ball:0>2d}', end=' ')
    print()


def random_select():
    """随机选择一组号码"""
    red_bills = [x for x in range(1, 34)]
    selected_bills = sample(red_bills, 6)
    selected_bills.sort()

    selected_bills.append(randint(1, 16))
    return selected_bills

n = int(input('机选几注：'))
for _ in range(n):
    display(random_select())