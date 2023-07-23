#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2019-12-22 11:35:22
lastTime: 2023-07-24 01:16:32
LastAuthor: Do not edit
FilePath: /Turing/13-协程/v09.py
Description: 
version: 
'''


import threading
import asyncio

@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    print('Start..... (%s)' % threading.currentThread())
    yield from asyncio.sleep(5)
    print('Done..... (%s)' % threading.currentThread())
    print('Hello again! (%s)' % threading.currentThread())

# 启动消息循环(去生成或获取一个事件循环)
loop = asyncio.get_event_loop()
# 定义任务
tasks = [hello(), hello()]
# 将任务放到任务列表(用于事件循环)
loop.run_until_complete(asyncio.wait(tasks)) # 多个子协程时,遇到io耗时会自动切换到其他子协程
# 关闭事件循环
loop.close()
