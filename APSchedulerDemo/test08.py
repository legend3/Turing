#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2021-04-09 07:31:12
lastTime: 2021-12-18 01:26:03
LastAuthor: Do not edit
FilePath: /Turing/APSchedulerDemo/test08.py
Description: 删除 job
当调度器中删除 job 时，该 job 也将从其关联的 job 存储中删除，并且将不再执行。有两种方法可以实现此目的：

通过调用方法 remove_job() ，指定 job ID 和 job 存储别名
通过调用 add_job() 时 返回的 apscheduler.job.Job 实例的 remove() 方法
version: 
'''

from apscheduler.schedulers.background import BackgroundScheduler
import time

def task():
    print("OK")

scheduler = BackgroundScheduler()
job = scheduler.add_job(task, 'interval', seconds=1, id='my_job_id')
scheduler.start()
time.sleep(3)
job.pause()
print("暂停job")
scheduler.resume_job('my_job_id')
print("恢复job")
scheduler.remove_job('my_job_id')
print("删除job")


# scheduler.add_job(jobs, 'interval', minutes=2, id='my_job_id')
# scheduler.remove_job('my_job_id')