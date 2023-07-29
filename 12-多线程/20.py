#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2019-12-22 11:35:22
lastTime: 2023-07-29 18:21:17
LastAuthor: Do not edit
FilePath: /Turing/12-多线程/20.py
Description: 
version: 
'''

import multiprocessing
from time import sleep, ctime


class ClockProcess(multiprocessing.Process):
    '''
        两个函数比较重要
            1. init构造函数
            2. run
    '''
    def __init__(self, interval):
        super().__init__() # 父类的构造函数
        self.interval = interval
    
    def run(self):
        while True:
            print("The time is %s" % ctime())
            sleep(self.interval)


if __name__ == '__main__':
    p = ClockProcess(3)
    p.start()
    
    # while True:
    #     print('sleeping.......')
    #     sleep(1)
    p.join() # 主进程让出给p进程(子进程结束，主进程才结束！)