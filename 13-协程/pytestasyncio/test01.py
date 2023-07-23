#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2021-12-17 01:05:20
lastTime: 2023-03-27 02:21:36
LastAuthor: Do not edit
FilePath: /Turing/13-协程/pytestasyncio/test01.py
Description: 
version: 
'''
import pytest
import asyncio

@pytest.mark.asyncio
async def test_sleep(event_loop):
    result = await asyncio.sleep(1, result=3, loop=event_loop)
    assert result == 3

@pytest.mark.asyncio
async def test_multiple_sleep(event_loop):
    tasks = [event_loop.create_task(asyncio.sleep(1, result=x))
             for x in range(10)]    # 定义任务
    results = await asyncio.gather(*tasks)  # 从给定的协程任务返回聚合结果
    print(results)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert results == list(range(10))
