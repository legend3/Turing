#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2019-12-22 11:35:22
lastTime: 2023-07-29 17:53:47
LastAuthor: Do not edit
FilePath: /Turing/12-多线程/24.py
Description: 
version: 
'''

import multiprocessing
from time import ctime

def consumer(input_q):
    print ("Into consumer:", ctime())
    while True:
        item = input_q.get()
        if item is None:
            break
        print("pull", item, "out of q")
    print ("Out of consumer:", ctime())

def producer(sequence, output_q):
    for item in sequence:
        print ("Into procuder:", ctime())
        output_q.put(item)
        print ("Out of procuder:", ctime())

if __name__ == '__main__':
    # 多个消费者
    q = multiprocessing.Queue()
    cons_p1 = multiprocessing.Process (target = consumer, args = (q,))
    cons_p1.start()

    cons_p2 = multiprocessing.Process (target = consumer, args = (q,))
    cons_p2.start()

    sequence = [1,2,3,4]
    producer(sequence, q)

    # 有几个子进程就放几个None，因为每个子进程取到None就会结束了，不影响其他子进程遇到None.
    q.put(None)
    q.put(None)

    cons_p1.join()
    cons_p2.join()
