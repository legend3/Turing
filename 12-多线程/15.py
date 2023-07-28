#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2019-12-22 11:35:22
lastTime: 2023-07-29 02:13:47
LastAuthor: Do not edit
FilePath: /Turing/12-多线程/15.py
Description: 
version: 
'''

import threading
import time

'''
(孙悟空大战沙僧)——解决死锁问题的措施
线程正处于阻塞状态,指当前线程执行过程中,所需要的资源长时间等待却一直未能获取到,被容器的线程管理器标识为阻塞状态,可以理解为等待资源超时的线程.

如果当前的状态为unlocked,则acquire()会将状态改为locked然后立即返回.
当状态为locked的时候,acquire()将被阻塞直到另一个线程中调用release()来将状态改为unlocked,然后acquire()才可以再次将状态置为locked.

Lock.acquire(blocking=True, timeout=-1),blocking参数表示是否阻塞当前线程等待,timeout表示阻塞时的等待时间.
如果成功地获得lock,则acquire()函数返回True,否则返回False,timeout超时时如果还没有获得lock仍然返回False.

'''
lock_1 = threading.Lock()
lock_2 = threading.Lock()

def func_1():
    print("func_1 starting.........")
    lock_1.acquire(timeout=4)   # 如果func_1调用lock_1锁,如果lock_1被别的线程正在获取,则等待(阻塞)4秒,四秒后未获取到则返回False,然后去进行一些其他的处理
    print("func_1 申请了 lock_1....")
    time.sleep(2)
    print("func_1 等待 lock_2.......")

    rst = lock_2.acquire(timeout=2)#只会花2秒钟等待申请lock2
    if rst:
        print("func_1 已经得到锁 lock_2")
        lock_2.release()
        print("func_1 释放了锁 lock_2")
    else:
        print("func_1 注定没申请到lock_2.....")

    lock_1.release()
    print("func_1 释放了 lock_1")

    print("func_1 done..........")


def func_2():
    print("func_2 starting.........")
    lock_2.acquire()
    print("func_2 申请了 lock_2....")
    time.sleep(4)
    print("func_2 等待 lock_1.......")
    lock_1.acquire()
    print("func_2 申请了 lock_1.......")

    lock_1.release()
    print("func_2 释放了 lock_1")

    lock_2.release()
    print("func_2 释放了 lock_2")

    print("func_2 done..........")


if __name__ == "__main__":

    print("主程序启动..............")
    t1 = threading.Thread(target=func_1, args=())
    t2 = threading.Thread(target=func_2, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("主程序结束..............")
