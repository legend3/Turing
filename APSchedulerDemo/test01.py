#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2021-04-09 07:31:12
lastTime: 2021-05-18 01:06:22
LastAuthor: Do not edit
FilePath: /Turing/APSchedulerDemo/test01.py
Description: 
Advanced Python Scheduler（APScheduler）是一个Python库，"可让您安排Python代码稍后执行"，一次或定期执行。 
您可以根据需要动态添加或删除旧作业。 如果将作业存储在数据库中，它们还将在调度程序重新启动并保持其状态的过程中幸免。 
重新启动调度程序后，它将运行脱机状态下应该运行的所有作业1。

除其他事项外，APScheduler可用作跨平台的，特定于应用程序的替代程序，以替换平台特定的计划程序，例如cron守护程序或Windows任务计划程序。 
但是请注意，APScheduler本身不是守护程序或服务，也不是任何命令行工具附带的。 它主要是要在现有应用程序中运行。 
也就是说，"APScheduler确实为您提供了一些构建块，以构建调度程序服务或运行专用的调度程序进程。"

APScheduler具有三个可以使用的内置调度系统：
    Cron-style方式的排程（具有可选的开始/结束时间）

    基于间隔的执行（以偶数间隔运行作业，并具有可选的开始/结束时间）

    一次性延迟执行（在设定的日期/时间运行一次作业）

您可以按自己喜欢的方式混合并匹配调度系统和存储作业的后端。 支持的用于存储作业的后端包括：
    Memory
    SQLAlchemy (any RDBMS supported by SQLAlchemy works)
    MongoDB
    Redis
    RethinkDB
    ZooKeeper

APScheduler还与几种常见的Python框架集成，例如：
    asyncio (PEP 3156)
    gevent
    Tornado
    Twisted
    Qt (using either PyQt , PySide2 or PySide)

有用于将APScheduler与其他框架集成的第三方解决方案：
    Django
    Flask
version: 
'''

from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()