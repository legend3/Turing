#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2019-12-22 11:35:22
lastTime: 2024-11-25 00:54:02
LastAuthor: Do not edit
FilePath: /Turing/12-多线程/16.py
Description: 
version: 
'''

import threading
import time

# 参数定义最多几个线程同时使用资源
semaphore = threading.Semaphore(3)

def func():
    if semaphore.acquire(): # 从semaphore中获取令牌(锁)，semaphore决定了最多能有几个线程能进入
        for i in range(5):
            print(threading.currentThread().getName() + ' get semaphore')
        time.sleep(5)
        semaphore.release() # 释放semaphore
        print(threading.currentThread().getName() + ' release semaphore')


for i in range(8):
    t1 = threading.Thread(target=func)
    t1.start()