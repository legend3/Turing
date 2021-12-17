#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2021-12-18 02:15:01
lastTime: 2021-12-18 03:30:38
LastAuthor: Do not edit
FilePath: /Turing/APSchedulerDemo/demo.py
Description: 
version: 
'''
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED
import time


def fun():
    # print("ok")
    return True


class S():
    retval = 0  # 静态变量
    def __init__(self):
        self.scheduler = BackgroundScheduler()  # 调度器
        self.scheduler.add_listener(self.listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)  # 监听器
        self.scheduler.start()  # 初始化，启动调度器
        
    def listener(self, event):
        retval = event.retval
        print(retval)

    def getResult(self):
        self.scheduler.add_job(
            fun,
            trigger='interval',
	        seconds=2
        )

    def start(self):
        self.scheduler.start()

    def shutdown(self):
        self.scheduler.shutdown()



class SS():
    def test(self):
        d = S()
        d.getResult()
        print(S.retval)
        time.sleep(60)


if __name__ == "__main__":
    ss = SS()
    ss.test()


# if __name__ == "__main__":
#     s = S()
#     s.start()
#     s.getResult()
#     print(S.retval)
#     time.sleep(60)
