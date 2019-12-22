#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @date:2019/04/11 16:17
# @name:write
# @author:lzg
import random
from pyhive import hive
import thrift
import sasl
import thrift_sasl


lename = ['Lily', 'Lilei', 'Smith', 'Jack', 'Mike', 'Allen', 'Ward', 'Kobe', 'Jones', 'Martin',
          'Blake','Clarl', 'Scott', 'Miller', 'Ford']
ljob = ['CLERK', 'ABALYST', 'MANAGER', 'SALESMAN', 'PRESIDENT']
lmgr = ['7902', '7698', '7839', '7566', '7788', '7782']
lhiredate = ['1980/12/17','1981/2/20','1981/2/22','1981/4/2','1981/9/28','1981/5/1','1981/6/9','1987/4/19',
             '198111/17','1981/9/8','1987/5/23','1981/12/3','1981/12/3','1982/1/23']
lsal = [800.00, 1600.00, 1250.00, 2975.00, 1250.00, 2850.00, 2450.00, 3000.00, 5000.00, 1500.00, 1100.00,
        5000.00, 1300.00]
lcomm = [0, 300.00, 500.00, 1400.00, ]
ldeptno = [10, 20, 30]
class HData:
    def __init__(self):
        self.empno = None
        self.ename = None
        self.job = None
        self.mgr = None
        self.hiredate = None
        self.sal = None
        self.comm = None
        self.deptno = None

    def make(self):
        count = 100000001
        for i in range(1,count):
            self.empno = i
            self.ename = random.choice(lename)
            self.job = random.choice(ljob)
            self.mgr = random.choice(lmgr)
            self.hiredate = random.choice(lhiredate)
            self.sal = random.choice(lsal)
            self.comm = random.choice(lcomm)
            self.deptno = random.choice(ldeptno)
            #写入文件
            with open("/opt/hivedata.txt",'a') as f:
                if i != count -1:
                    f.write(str(self.empno) + "," + str(self.ename) + "," + str(self.job) + "," + str(self.mgr) + "," + str(self.hiredate) + "," + str(self.sal) + "," + str(self.comm) + "," + str(self.deptno) + "\n")
                else:
                    f.write(str(self.empno) + "," + str(self.ename) + "," + str(self.job) + "," + str(self.mgr) + "," + str(self.hiredate) + "," + str(self.sal) + "," + str(self.comm) + "," + str(self.deptno))
                print(u'已执行：' + str(i) + u'次')
#
# class CreateHiveTable:
#     def __init__(self):
#         self.conn = None
#         self.cursor = None
#
#     def make(self):
#         self.conn = hive.Connection(host='192.168.0.71', port=10000, username ='admin', password='admin', database='default')#username = 'yuzhibo',    auth="NOSAL"
#         print self.conn,":对接Hive成功！"
#         self.cursor.execute("create table if not exists zhenguo(empno int, ename string, job string,mgr int,hiredate Date comment 'The higher number',sal double comment 'salary',comm double comment 'commission') ROW FORMAT DELIMITED FIELDS TERMINATED BY '\func';")
#         print '表创建完毕！'
# # class PHive():
# #     def __init__(self):
# #         self.conn = None
# #         self.cursor = None
# #
# #     def conn(self):
# #         self.conn = hive.Connection(host='192.168.0.71', port='10000', username = 'yuzhibo', database = 'default')
# #         print(self.conn,":对接Hive成功！")
# #         self.cursor.execute("load data local inpath \'/home/admin/test_dir/hivedata.txt\' overwrite into table zhenguo;")
#
#
if __name__ == '__main__':
        HData().make()
    # CreateHiveTable().conn

conn = hive.Connection(host='192.168.0.71', port=10000, database='default',auth='NOSASL')
cursor=conn.cursor()
cursor.execute("create table if not exists zhenguo(empno int, ename string, job string,mgr int,hiredate Date comment 'The higher number',sal double comment 'salary',comm double comment 'commission') ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';")
print("完成！")