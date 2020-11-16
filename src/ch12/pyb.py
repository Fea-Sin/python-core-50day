#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 8e04fa1745d9e5b2ec7def478117f096
# @Time   : 2020/11/16 2:06 下午
# @Author : FEASIN

import requests
import json

APIKEY = ''
num = 10
rand = 1

def get_img(page=1):
    resp = requests.get(f'http://api.tianapi.com/meinv/index?key={APIKEY}&num={num}&page={page}&rand={rand}')

    # 通过Response对象的content属性获取服务器返回的二进制内容
    if resp.status_code == 200:
        data = resp.json()
        for item in data['newslist']:
            imgdata = requests.get(item['picUrl'])
            with open('one/' + item['title'] + '.jpg', 'wb') as file:
                file.write(imgdata.content)

# get_img()

for index in range(2, 6):
    get_img(index)

print('程序执行结束')








