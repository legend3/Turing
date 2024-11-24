#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2019-12-22 11:35:22
lastTime: 2024-11-25 01:55:52
LastAuthor: Do not edit
FilePath: /Turing/12-多线程/18.py
Description: 
version: 
'''

import threading
import time

'''
递归时,最初自己申请了锁,又没归还,又会要申请锁(会死锁)
RLock可以解决这个问题
'''
class MyThread(threading.Thread):
    def run(self):
        global num
        # time.sleep(1)

        if mutex.acquire(1): # acquire(timeout=1)
            num = num + 1
            msg = self.name + ' set num to '+str(num)
            print(msg)
            time.sleep(3)
            mutex.acquire()
            print(self.name + ' 又获取到锁了！' + mutex.__str__())
            mutex.release()
            mutex.release()

num = 0

mutex = threading.RLock() # 可重用锁,"大锁"


def testTh():
    for i in range(5):
        t = MyThread()
        t.start()


if __name__ == '__main__':
    testTh()



'''
    使用了 RLock,与普通的 Lock 不同,RLock 允许同一个线程多次获得锁而不会死锁。
'''

