#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/10 11:08 上午
# @Author : FEASIN

import random

ALL_CHARS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def generate_code(code_len=4):
    """
    生成指定长度的验证码
    :param code_len:
    :return: 由大小写英文字母和数字构成的随机验证码字符串
    """
    code = ''
    for _ in range(code_len):
        index = random.randrange(0, len(ALL_CHARS))
        code += ALL_CHARS[index]

    # 打印输出
    print(code)

    return code

for _ in range(10):
    generate_code()