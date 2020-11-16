#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/16 10:40 上午
# @Author : FEASIN

import json

my_dict = {
    'name': '骆昊',
    'age': 40,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}

with open('one.json', 'w', encoding='utf-8') as file1:
    json.dump(my_dict, file1)

dict_json = json.dumps(my_dict)

print('json dumps---', dict_json)

with open('two.json', 'w', encoding='utf-8') as file2:
    file2.write(dict_json)

print('字典已经保存到文件中')