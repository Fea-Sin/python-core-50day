#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/13 3:28 下午
# @Author : FEASIN

import base64

content = 'Man is distinguished, not only by his reason'

# 二进制编码
# print('这个编码是啥---', content.encode())

# base64 编码
content_base64 = base64.b64encode(content.encode())
print('base64编码--', content_base64)

# base64 解码
print('base64解码--', base64.b64decode(content_base64).decode())