#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 8e04fa1745d9e5b2ec7def478117f096
# @Time   : 2020/11/16 11:24 上午
# @Author : FEASIN

import requests
import json

APIKEY = ''
num = 30

resp = requests.get(f'http://api.tianapi.com/woman/index?key={APIKEY}&num={num}')
if resp.status_code == 200:
    data_model = resp.json()

    # 数据持久化
    # with open('news.json', 'w') as file:
    #     json.dump(data_model, file)

    # 打印输出
    for news in data_model['newslist']:
        print(news['title'])
        print(news['url'])
        print('-' * 60)

print('程序运行结束')
