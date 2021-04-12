#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2021-04-09 07:31:12
lastTime: 2021-04-09 07:40:51
LastAuthor: Do not edit
FilePath: /Turing/APSchedulerDemo/test07.py
Description: date：某个特定时间仅运行一次 job
version: 
'''

import datetime
from apscheduler.schedulers.background import BackgroundScheduler


def job():
	print('job')

scheduler = BackgroundScheduler()
scheduler.start()

# 3 秒后运行
scheduler.add_job(
	job,
	trigger='date',
	run_date=datetime.datetime.now() + datetime.timedelta(seconds=3)
)

# 2019.11.22 00:00:00 运行
scheduler.add_job(
	job,
	trigger='date',
	run_date=datetime.date(2019, 11, 22),
)

# 2019.11.22 16:30:01 运行
scheduler.add_job(
	job,
	trigger='date',
	run_date=datetime.datetime(2019, 11, 22, 16, 30, 1),
)

# 2019.11.31 16:30:01 运行
scheduler.add_job(
	job,
	trigger='date',
	run_date='2019-11-31 16:30:01',
)

# 立即运行
scheduler.add_job(
	job,
	trigger='date'
)
