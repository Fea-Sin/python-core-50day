#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/18 6:00 下午
# @Author : FEASIN

"""
删除一个部门

如果不希望每次SQL操作之后手动提交或回滚事务，
在创建连接的时候加一个名为`autocommit`的参数并将它的值设置为`True`
表示每次执行SQL之后自动提交。
如果程序中不需要使用事务环境也不希望手动的提交或回滚就可以如此
"""

import pymysql

def main():
    no = int(input('编码：'))
    con = pymysql.connect(
        host='localhost',
        port=3306,
        database='hrs',
        charset='utf8',
        user='root',
        password='cqz123456',
        autocommit=True
    )
    try:
        with con.cursor() as cursor:
            result = cursor.execute(
                'delete from tb_dept where dno=%s',
                (no)
            )
        if result == 1:
            print('数据删除成功')
    finally:
        con.close()

if __name__ == '__main__':
    main()
