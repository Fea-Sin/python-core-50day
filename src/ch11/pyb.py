#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/16 11:07 上午
# @Author : FEASIN

import json

with open('one.json', 'r') as file:
    my_dict = json.load(file)
    print(type(my_dict))
    print(my_dict)
    print('获取数据----', my_dict['name'])