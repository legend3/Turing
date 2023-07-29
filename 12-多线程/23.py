#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2019-12-22 11:35:22
lastTime: 2023-07-29 17:50:06
LastAuthor: Do not edit
FilePath: /Turing/12-多线程/23.py
Description: 
version: 
'''


import multiprocessing
from time import ctime

# 设置哨兵问题
def consumer(input_q):
    print("Into consumer:", ctime())
    while True:
        item = input_q.get() # 哨兵值
        if item is None:
            break # 结束子进程！
        print("pull", item, "out of q")
    print ("Out of consumer:", ctime()) ## 此句执行完成，再转入主进程


def producer(sequence, output_q):
    print ("Into procuder:", ctime())
    for item in sequence:
        output_q.put(item)
        print ("put", item, "into q")
    print ("Out of procuder:", ctime())


if __name__ == '__main__':
    q = multiprocessing.Queue()
    cons_p = multiprocessing.Process(target = consumer, args = (q,))
    cons_p.start()

    sequence = [1,2,3,4]
    producer(sequence, q)

    q.put(None) # 列表中放入一个None，给“哨兵”用的
    cons_p.join()