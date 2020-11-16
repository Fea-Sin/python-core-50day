#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/16 2:58 下午
# @Author : FEASIN

import random
import re
import time

import requests

for page in range(1, 11):
    resp = requests.get(
        # start 参数代表从哪一部电影开始
        url=f'https://movie.douban.com/top250?start={(page - 1) * 25}',
        # 如果不设置HTTP请求头中的User-Agent，豆瓣会检测出是爬虫程序而阻止我们的请求
        # User-Agent可以设置为浏览器的标识（可以在浏览器的开发者工具查看HTTP请求头）
        headers={'User-Agent': 'BaiduSpider'}
    )
    # 创建正则表达式对象，通过捕获组捕获span标签中的电影标题
    pattern = re.compile(r'\<span class="title"\>([^&]*?)\<\/span\>')
    # 通过正则表达式获取class属性为title且标签内容不以&符号开头的span标签
    results = pattern.findall(resp.text)

    with open('two/movie.txt', 'a', encoding='utf-8') as file:
        for result in results:
            file.write(f'\n{result}')

    time.sleep(random.randint(1, 3))


print('程序执行结束')

