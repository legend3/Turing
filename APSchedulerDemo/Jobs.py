#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2021-12-18 02:15:01
lastTime: 2021-12-20 02:49:15
LastAuthor: Do not edit
FilePath: /Turing/APSchedulerDemo/Jobs.py
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
class AddJobs():
    def __init__(self):
        global scheduler
        self.response = None
        scheduler = BackgroundScheduler()  # 调度器
        # self.job = scheduler.add_job(fun,trigger='interval',seconds=2,id='myJobId') # 添加job
        # scheduler.start()  # 初始化，启动调度器
    
    def getResponse(self):
        return self.response
    
    def listener(self, event):
        self.response = event.retval
        if event.exception:
            print(event.exception)
        else:
            if self.response > 2:
                # print("定时任务线程--", threading.currentThread().getName())  # 当前线程-- APScheduler
                # 运行中删除job
                # self.scheduler.remove_job('myJobId')  # thread APScheduler的scheduler删除job
                scheduler.remove_job('myJobId')  # thread main的scheduler删除job    (全局变量由main线程操作)
                print("my job is remove: ", scheduler.get_job('myJobId'))

    def setJobs(self, fun):
        # 添加jobs
        scheduler.add_job(
            fun,
            trigger='interval',
	        seconds=2,
            id='myJobId'
        )
        # 添加监听器
        scheduler.add_listener(self.listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)  # 监听器

    def start(self):
        scheduler.start()

    def shut(self):
        scheduler.remove_all_jobs()

    def remove(self, jobId):
        scheduler.remove_job(jobId)


# if __name__ == "__main__":
#     s = S()
#     s.setJobs(fun)
#     s.start()
#     print(s.getResponse())
#     time.sleep(3)  # 等待接口响应
#     print("当前线程--", threading.currentThread().getName())  # 当前线程-- MainThread
#     s.remove('myJobId')  # (要等到BackgroundScheduler线程执行完job)要用主线程删除
#     time.sleep(60)  # 保持main线程运行状态
