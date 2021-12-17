#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2021-04-09 07:31:35
lastTime: 2021-12-18 05:24:26
LastAuthor: Do not edit
FilePath: /Turing/APSchedulerDemo/test09.py
Description: 
version: 
'''


from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED
from datetime import datetime, timedelta
import logging


times = 0
def fn():
    '''Increase `times` by one and print it.'''
    global times
    times += 1
    print(times)
    return times

def fn2():
    print(f"我爱{times}")

def my_listener(event):
    if event.exception:
        print('The job crashed :(')
    else:
        if event.retval == 4:
            scheduler.remove_job('addTimes')
            print(scheduler.get_job('addTimes'))  # 检查job是否被成功删除
            scheduler.add_job(fn2, trigger=CronTrigger(second='*/1'), id='say love!')
        

scheduler = BlockingScheduler()
# Execute fn() each second.
scheduler.add_job(fn, trigger=CronTrigger(second='*/1'), id='addTimes')
scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)  # 监听器
scheduler.start()











# def run_all():
#     return True


# def job_runs(event):  # listener function
#     if event.exception:
#         print('The job did not run')
#     else:
#         print('The job completed @ {}'.format(datetime.now()))


# def job_return_val(event):  # listener function
#     return event.retval


# scheduler = BackgroundScheduler()
# scheduler.add_listener(job_runs, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
# scheduler.add_listener(job_return_val, EVENT_JOB_EXECUTED)
# # cron_args = datetime_to_dict(datetime.now() + timedelta(minutes=1))
# job = scheduler.add_job(run_all, "cron", second='*/10')

# test = scheduler.start()
# scheduler.print_jobs()
# logging.basicConfig()
# logging.getLogger('apscheduler').setLevel(logging.DEBUG)