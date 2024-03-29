#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2019-12-22 11:35:22
lastTime: 2023-07-28 03:11:22
LastAuthor: Do not edit
FilePath: /Turing/12-多线程/09.py
Description: 
version: 
'''

import threading
import time

# 1. 类需要继承自threading.Thread
class MyThread(threading.Thread):
    def __init__(self, arg):
        super(MyThread, self).__init__()
        self.arg = arg

    # 2 必须重写run函数，run函数代表的是真正执行的功能
    def run(self):
        time.sleep(2)
        print("The args for this class is {0}".format(self.arg))

for i in range(5):
    t = MyThread(i) # 线程实例化
    t.start()
    # t.join()

print("Main thread is done!!!!!!!!")