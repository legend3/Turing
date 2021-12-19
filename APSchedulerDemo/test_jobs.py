#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

'''
Author: LEGEND
since: 2021-05-18 01:10:13
lastTime: 2021-12-18 17:19:19
LastAuthor: Do not edit
FilePath: /Turing/APSchedulerDemo/test_apscheduler.py
Description: 
version: 
'''
import sys, os
import time
import threading
# sys.path.append(os.path.abspath(os.path.join(os.path.split(os.path.abspath(__file__)[0])), '../'))
from APSchedulerDemo.Jobs import AddJobs

a = 0
def test():
    global a
    a += 1
    return a

@pytest.mark.parametrize('case', [1,2])
def test01(case):
    addJobs = AddJobs()
    addJobs.setJobs(test)
    addJobs.start()
    time.sleep(5)  # 接口响应时间
    print(addJobs.getResponse())
    # print("当前线程--", threading.currentThread().getName())  # 当前线程-- MainThread
    # s.remove()  # (要等到BackgroundScheduler线程执行完job)要用主线程删除