#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pytest
import os

'''
@Author: LEGEND
@since: 2020-04-25 13:07:55
@lastTime: 2020-05-17 16:20:49
@FilePath: \Turing\20-MySQL\Demo.py
@Description: 
@version: 
'''


def test_mysql(con):
    try:
        # print(con)
        # con = pymysql.connect(host='localhost', user='root', password='root', port=3306, 
        #                         db='cloud_note', 
        #                         charset='utf8mb4')
        cur = con.cursor()
        cur.execute('select cn_note_id from cn_note;')
        for result in cur.fetchall():
            if result[0] == 'IDLE':
                print(result[0])
                
        print("\n结果:", result)
    except Exception as e:
        print("操作数据库异常：", e)


if __name__ == "__main__":
    # print(os.getcwd())
    pytest.main(['-vs', './20-MySQL/Demo.py::test_mysql'])