#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2023-07-24 00:20:20
lastTime: 2023-07-24 00:20:27
LastAuthor: Do not edit
FilePath: /Turing/13-协程/小白教程/demo1.py
Description: 
version: 
'''

import asyncio

@asyncio.coroutine
def func1():
    print(1)
    yield from asyncio.sleep(2)  # 遇到IO耗时操作，自动化切换到tasks中的其他任务
    print(2)


@asyncio.coroutine
def func2():
    print(3)
    yield from asyncio.sleep(2) # 遇到IO耗时操作，自动化切换到tasks中的其他任务
    print(4)


tasks = [
    asyncio.ensure_future( func1() ),
    asyncio.ensure_future( func2() )
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))