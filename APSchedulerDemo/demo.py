#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2021-12-18 02:15:01
lastTime: 2021-12-18 16:53:53
LastAuthor: Do not edit
FilePath: /Turing/APSchedulerDemo/demo.py
Description: 区分scheduler对象的占有线程, thread APScheduler or thread main?
version: 
'''
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED
import time
import threading


# def fun():
#     return True

scheduler = None
class S():
    def __init__(self):
        global scheduler
        self.res = None
        scheduler = BackgroundScheduler()  # 调度器
        # self.job = scheduler.add_job(fun,trigger='interval',seconds=2,id='myJobId') # 添加job
        # scheduler.start()  # 初始化，启动调度器
    
    def getResult(self):
        return self.res
    
    def listener(self, event):
        self.res = event.retval
        if event.exception:
            print('The job crashed :(')
        else:
            if self.res > 2:
                # print("定时任务线程--", threading.currentThread().getName())  # 当前线程-- APScheduler
                # self.scheduler.remove_job('myJobId')  # thread APScheduler的scheduler删除job
                scheduler.remove_job('myJobId')  # thread main的scheduler删除job    (全局变量由main线程操作)
                print("my job is remove: ", scheduler.get_job('myJobId'))

    def setJob(self, fun):
        scheduler.add_job(
            fun,
            trigger='interval',
	        seconds=2,
            id='myJobId'
        )
        scheduler.add_listener(self.listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)  # 监听器

    def start(self):
        scheduler.start()

    # def shut(self):
    #     scheduler.remove_all_jobs()

    def remove(self):
        scheduler.remove_job('myJobId')


# if __name__ == "__main__":
#     s = S()
#     s.setJob(fun)
#     s.start()
#     print(s.getResult())
#     time.sleep(3)
#     print("当前线程--", threading.currentThread().getName())  # 当前线程-- MainThread
#     s.remove()  # (要等到BackgroundScheduler线程执行完job)要用主线程删除
#     time.sleep(60)
