#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2021-04-09 07:31:12
lastTime: 2021-04-09 08:04:25
LastAuthor: Do not edit
FilePath: /Turing/APSchedulerDemo/test05.py
Description: 
version: 
'''

import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import time


def job1():
	print('job1')


def job2(x, y):
	print('job2', x, y)


scheduler = BackgroundScheduler()


# 间隔3s运行一次
scheduler.add_job(
	job1,
	trigger='cron',
	second=3
)

# # 间隔3s运行一次
# scheduler.add_job(
# 	job1,
# 	trigger='cron',
# 	second=3
# )

# # 每天 2 点运行
# scheduler.add_job(
# 	job1,
# 	trigger='cron',
# 	hour=2
# )

# # 每天 2 点 30 分 5 秒运行
# scheduler.add_job(
# 	job2,
# 	trigger='cron',
# 	second=5,
# 	minute=30,
# 	hour=2,
# 	args=['hello', 'world']
# )

# # 每 10 秒运行一次
# scheduler.add_job(
# 	job1,
# 	trigger='cron',
# 	second='*/10'
# )

# # 每天 1:00,2:00,3:00 运行
# scheduler.add_job(
# 	job1,
# 	trigger='cron',
# 	hour='1-3'
# )

# # 在 6,7,8,11,12 月的第三个周五 的 1:00,2:00,3:00 运行
# scheduler.add_job(
# 	job1,
# 	trigger='cron',
# 	month='6-8,11-12',
# 	day='3rd fri',
# 	hour='1-3'
# )

# # 在 2019-12-31 号之前的周一到周五 5 点 30 分运行
# scheduler.add_job(
# 	job1,
# 	trigger='cron',
# 	day_of_week='mon-fri',
# 	hour=5,
# 	minute=30,
# 	end_date='2019-12-31'
# )
scheduler.start()
time.sleep(60)