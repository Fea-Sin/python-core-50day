#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/16 6:08 下午
# @Author : FEASIN

from bs4 import BeautifulSoup
import requests
from collections import Counter
from os import path

# resp = requests.get(
#     url='https://movie.douban.com',
#     headers={
#         'User-Agent': 'BaiduSpider'
#     }
# )

def get_movie():
    resp = requests.get(
        url='https://movie.douban.com',
        headers={
            'User-Agent': 'BaiduSpider'
        }
    )
    return BeautifulSoup(resp.text, 'lxml')


# 标签集合
def get_all_tag_name():
    soup = get_movie()
    tag_set = set()
    for tag in soup.find_all(True):
        tag_set.add(tag.name)
    print('所有标签----', tag_set)


# 返回所有内容
def get_all_img():
    soup = get_movie()
    name = 1
    for tag in soup.find_all(['img']):
        try:
            src = tag['src']
            name += 1
            _, ext = path.splitext(src)
            imgdata = requests.get(src)
            with open('one/' + str(name) + ext, 'wb') as file:
                file.write(imgdata.content)

        except:
            print('这里有一个没有匹配')

    print('程序执行结束')






