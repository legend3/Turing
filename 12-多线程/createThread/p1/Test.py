#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2021-05-23 20:01:07
lastTime: 2021-05-23 20:18:29
LastAuthor: Do not edit
FilePath: /Turing/12-多线程/createThread/p1/test.py
Description: 
version: 
'''

from MyThread import MyThread


if __name__ == "__main__":
    mythread = MyThread("first")
    mythread.start()
    print("main完毕....")