#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/19 10:23 上午
# @Author : FEASIN
import pymysql

def condata():
    return pymysql.connect(
        host='localhost',
        port=3306,
        database='hrs',
        charset='utf8',
        user='root',
        password='cqz123456',
        autocommit=True
    )