#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2019-12-22 11:35:22
lastTime: 2023-07-29 02:48:57
LastAuthor: Do not edit
FilePath: /Turing/12-多线程/17.py
Description: 
version: 
'''

import threading
import time

def func():
    print("I am running.........")
    time.sleep(4)
    print("I am done......")



if __name__ == "__main__":
    t = threading.Timer(6, func) # 6秒后启动线程启动执行func函数
    t.start()

    i = 0
    while True:
        print("{0}***************".format(i))
        time.sleep(3)
        i += 1
