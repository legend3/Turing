#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2019-12-22 11:35:22
lastTime: 2024-11-24 01:27:34
LastAuthor: Do not edit
FilePath: /Turing/12-多线程/07.py
Description: 
version: 
'''

import time
import threading

def fun():
    print("Start fun")
    time.sleep(2)
    print("end fun")

print("Main thread")

t1 = threading.Thread(target=fun, args=() )
# 设置守护线程的方法，必须在start之前设置，否则无效
t1.setDaemon(True)# 这样主线程终端后,会自动中断守护线程
# t1.daemon = True
t1.start()

time.sleep(1)
print("Main thread end")
