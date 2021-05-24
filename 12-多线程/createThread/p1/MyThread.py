#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2021-05-23 20:02:29
lastTime: 2021-05-23 20:28:54
LastAuthor: Do not edit
FilePath: /Turing/12-多线程/createThread/p1/MyThread.py
Description: 
version: 
'''

import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name=None):
        super(MyThread, self).__init__(name=name)
        print(f"当前线城是: {threading.currentThread().getName()}")

    def run(self):
        time.sleep(2)
        print(f"{threading.current_thread().getName()}完毕.....")


if __name__ == "__main__":
    mythread = MyThread(name="我的线程")
    # mythread.setName("mythread")
    mythread.start()
    print(f"{threading.currentThread().getName()}完毕....")