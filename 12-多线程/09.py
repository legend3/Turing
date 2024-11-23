#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2019-12-22 11:35:22
lastTime: 2024-11-24 01:43:24
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

    # 2 必须重写run函数,run函数代表的是真正执行的功能
    def run(self):
        time.sleep(2)
        print("The args for this class is {0}".format(self.arg))

if __name__ == '__main__':
    for i in range(5):
        t = MyThread(i) # 线程实例化
        t.start()
        # t.join()

    print("Main thread is done!!!!!!!!")


'''
    优点：
        高灵活性：可以添加更多属性和方法,封装复杂逻辑。
        易扩展：通过继承和重写方法,可以扩展线程行为（如初始化数据、处理状态等）。
        逻辑清晰：线程相关的逻辑封装在类中,职责分明。
    缺点：
        代码复杂度较高：需要定义类,增加了额外的代码。
        对于简单任务显得冗长：不如第一种方式(03.py)直观简洁。
'''

'''
    即使主线程结束了,Python 的 线程管理机制 会确保所有子线程在执行完成后再退出程序。这是由 Python 主线程和子线程的生命周期管理 决定的。

    主线程与子线程的关系
        1.主线程的行为：
            主线程是程序的入口点,执行 if __name__ == '__main__': 中的代码。
            当主线程完成其代码后,它不会立即退出,而是会等待所有非守护线程（默认情况下,Python 的线程是非守护线程）完成后再退出。
        2.子线程的行为：
            子线程在主线程调用 t.start() 后开始运行,但它们是独立的,运行在并发环境中。
            主线程完成后,会检查是否还有未完成的非守护线程,如果有,主线程会等待这些线程完成。
'''