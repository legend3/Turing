#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2021-12-18 02:15:01
lastTime: 2021-12-18 05:37:22
LastAuthor: Do not edit
FilePath: /Turing/APSchedulerDemo/demo.py
Description: 
version: 
'''
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED
import time
import threading


def fun():
    return True


class S():
    def __init__(self):
        self.res = None
        self.scheduler = BackgroundScheduler()  # 调度器
        # self.job = self.scheduler.add_job(fun,trigger='interval',seconds=2,id='my_job_id') # 添加job
        # self.scheduler.start()  # 初始化，启动调度器
    
    def getRes(self):
        return self.res
    
    def listenerInfo(self, event):
        self.res = event.retval
        if event.exception:
            print('The job crashed :(')
        else:
            if self.res == True:
                print("当前线程--", threading.currentThread().getName())  # 当前线程-- APScheduler
                # self.scheduler.remove_job('my_job_id')  # scheduler线程删除报错
                
    def setJob(self):
        self.scheduler.add_job(
            fun,
            trigger='interval',
	        seconds=2,
            id='my_job_id'
        )
        self.scheduler.add_listener(self.listenerInfo, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)  # 监听器

    def start(self):
        self.scheduler.start()

    # def shut(self):
    #     self.scheduler.remove_all_jobs()

    def remove(self):
        self.scheduler.remove_job('my_job_id')





if __name__ == "__main__":
    s = S()
    s.setJob()
    s.start()
    print(s.getRes())
    time.sleep(3)
    print("当前线程--", threading.currentThread().getName())  # 当前线程-- MainThread
    s.remove()  # (要等到BackgroundScheduler线程执行完job)要用主线程删除
    time.sleep(60)
