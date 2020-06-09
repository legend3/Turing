#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2020-06-09 23:53:36
@lastTime: 2020-06-10 00:08:19
@LastAuthor: Do not edit
@FilePath: \Turing\Pytest_learning\Python Testing with pytest\pytest-parallel\tests\testdemo.py
@Description: pytest-parallel支持python3.6及以上版本，如果是想做多进程并发的需要在linux平台或mac上做，
                windows上不起作用即(workers永远=1)，
                    如果是做多线程的Linux/Mac/Windows平台都支持，进程数为workers设置的值。
    安装：pip install pytest-parallel
    pytest test.py --workers 3：3个进程运行
    pytest test.py --tests-per-worker 4：4个线程运行
    pytest test.py --workers 2 --tests-per-worker 4：2个进程并行，且每个进程最多4个线程运行，即总共最多8个线程运行。
@version: 
'''
import pytest


@pytest.mark.parametrize('items', [1,2,3])
def test_parallel(items):
    print(items)    