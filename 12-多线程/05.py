#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2019-12-22 11:35:22
lastTime: 2023-07-28 02:49:37
LastAuthor: Do not edit
FilePath: /Turing/12-多线程/05.py
Description: 
version: 
'''


#利用time延时函数，生成两个函数
# 利用多线程调用
# 计算总运行时间
# 练习带参数的多线程启动方法
import time
# 导入多线程处理包
import threading

def loop1(in1):
    # ctime 得到当前时间
    print('Start loop 1 at :', time.ctime())
    # 把参数打印出来
    print("我是参数 ",in1)
    # 睡眠多长时间，单位是秒
    time.sleep(4)
    print('End loop 1 at:', time.ctime())

def loop2(in1, in2):
    # ctime 得到当前时间
    print('Start loop 2 at :', time.ctime())
    # 把参数in 和 in2打印出来，代表使用
    print("我是参数 " ,in1 , "和参数  ", in2)
    # 睡眠多长时间，单位是秒
    time.sleep(2)
    print('End loop 2 at:', time.ctime())


if __name__ == "__main__":
    print("Starting at:", time.ctime())
    # 生成threading.Thread实例
    t1 = threading.Thread(target=loop1, args=("王老大",))
    t1.start()

    t2 = threading.Thread(target=loop2, args=("王大鹏", "王小鹏"))
    t2.start()

    t1.join() # 当前线程等待t1执行完
    t2.join() # 当前线程等待t2执行完

    print("All done at:", time.ctime())
    # 一定要有while语句
    # 因为启动多线程后本程序就作为主线程存在
    # 如果主线程执行完毕，则子线程可能也需要终止
    # while True:
    #     time.sleep(10)
