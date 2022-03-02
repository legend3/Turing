#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2022-03-02 19:28:50
lastTime: 2022-03-02 19:37:53
LastAuthor: Do not edit
FilePath: /Turing/12-多线程/25.py
Description: 并行
version: 
'''


from multiprocessing import Pool, Manager, queues
import multiprocessing, queue, time

def fun(que, filename):
    '''消费者'''
    while True:
        # print(que.qsize())
        try:
            item = que.get(block=False) # 获取队列值
        except queue.Empty:
            break
        print('输出数字：' + item + f'，输入至文件{filename}')

def run(process_num, x, filename):
    '''生产者'''
    manager = multiprocessing.Manager() # 多进程间建立通信
    que = manager.Queue() # 建立进程队列
    for i in x:
        que.put(i) # 写入队列
    pool = Pool(process_num) # 创建进程池
    filename_arg = [f'{filename}_{num}' for num in range(process_num)]
    args = [[que, filename_arg[i]] for i in range(process_num)] # 根据进程池数据量配置进程参数
    pool.starmap(fun, args) # 同步执行
    pool.close() # 关闭线程池，不再接受新的进程
    pool.join() # 阻塞主进程，等待子进程退出


if __name__=='__main__':
    run(process_num=2, x=[f'{num}' for num in range(5)], filename='filename')
