#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pymysql

'''
@Author: LEGEND
@since: 2020-04-25 13:07:55
@lastTime: 2020-04-25 15:03:49
@FilePath: \Turing\20-MySQL\Demo.py
@Description: 
@version: 
'''


def test_mysql(connection):
    assert isinstance(connection, pymysql)
    try:
        cur = pymysql.connect().cursor()
        pymysql.
    except Exception as e:
        print("操作数据库异常：", e)
    else:
        pass


@pytest.fixture()
def connection():
    try:
        con = pymysq.connect(host='localhost', user='root', password='root', port=3306, db='mydata', charset='utf8mb4')
        print("连接数据路成功！")
        return con
    except Exception as e:
        print("数据库连接异常", e)
    finally:
        con.close()
        print("断开数据库！")