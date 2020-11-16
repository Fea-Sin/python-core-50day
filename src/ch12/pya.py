#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/16 2:01 下午
# @Author : FEASIN

import requests

resp = requests.get('https://www.sohu.com/')

# 通过Response对象的text属性获取服务器返回的文本内容
if resp.status_code == 200:
    print('返回数据内容----', resp.text)