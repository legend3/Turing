#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2019-12-22 11:35:22
lastTime: 2023-07-28 03:30:57
LastAuthor: Do not edit
FilePath: /Turing/12-多线程/12.py
Description: 
version: 
'''

import threading
'''
线程不安全，加锁
'''
sum = 0
loopSum = 1000000

#创建锁实例
lock = threading.Lock()


def myAdd():
    global  sum, loopSum

    for i in range(1, loopSum):
        # 上锁，申请锁
        lock.acquire()
        sum += 1
        # 释放锁
        lock.release()


def myMinu():
    global  sum, loopSum
    for i in range(1, loopSum):
        lock.acquire()
        sum -= 1
        lock.release()


if __name__ == '__main__':
    print("Starting ....{0}".format(sum))

    # 开始多线程的实例，看执行结果是否一样
    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinu, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done .... {0}".format(sum))
