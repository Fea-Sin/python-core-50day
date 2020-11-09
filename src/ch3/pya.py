#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/9 6:14 下午
# @Author : FEASIN

"""
滚动文字

version 0.1
"""

import os
import time

content = '北 京 欢 迎 你 为 你 开 天 辟 地      '

while True:
    os.system('clear')
    print(content)
    time.sleep(0.2)
    content = content[1:] + content[0]