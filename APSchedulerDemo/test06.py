#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2021-04-09 07:31:12
lastTime: 2021-12-18 02:11:32
LastAuthor: Do not edit
FilePath: /Turing/APSchedulerDemo/test06.py
Description: interval：以固定的时间间隔运行 job

主要参数：

weeks(int) - 表示等待时间的周数

days(int) - 表示等待时间天数

hours(int) - 表示等待时间小时数

minutes(int) - 表示等待时间分钟数

seconds(int) - 表示等待时间秒数

start_date(date|datetime|str) - 开始时间

end_date(date|datetime|str) - 结束时间
version: 
'''

from apscheduler.schedulers.background import BackgroundScheduler
import time
from apscheduler.executors.pool import ThreadPoolExecutor


def job():
	print('job')

scheduler = BackgroundScheduler()


# 每 2 小时运行一次
scheduler.add_job(
	job,
	trigger='interval',
	hours=2
)

# # 2019-10-01 00:00:00 到 2019-10-31 23:59:59 之间每 2 小时运行一次
# scheduler.add_job(
# 	job,
# 	trigger='interval',
# 	hours=2,
# 	start_date='2019-10-01 00:00:00',
# 	end_date='2019-10-31 23:59:59',
# )

# # 每 2 天 3 小时 4 分钟 5 秒 运行一次
# scheduler.add_job(
# 	job,
# 	trigger='interval',
# 	days=2,
# 	hours=3,
# 	minutes=4,
# 	seconds=5
# )
scheduler.start()
time.sleep(60)