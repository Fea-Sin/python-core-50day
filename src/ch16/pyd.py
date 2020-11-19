#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/19 10:21 上午
# @Author : FEASIN

from pymysql.cursors import DictCursor

import condata

def main():
    con = condata.condata()

    try:
        with con.cursor(cursor=DictCursor) as cursor:
            cursor.execute(
                'select dno as no, dname as name, dloc as loc from tb_dept'
            )
            results = cursor.fetchall()
            print('查询所有数据', results)
            print('编号\t名称\t\t所在地')
            for dept in results:
                print(dept['no'], end='\t')
                print(dept['name'], end='\t')
                print(dept['loc'], end='\n')
    finally:
        con.close()

if __name__ == '__main__':
    main()



