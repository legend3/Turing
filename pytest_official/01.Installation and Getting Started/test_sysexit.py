#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2020-08-01 20:52:57
@lastTime: 2020-08-01 20:56:52
@LastAuthor: Do not edit
@FilePath: \Turing\Python_Testing_with_pytest\pytest_official\01.Installation and Getting Started\test_sysexit.py
@Description: 
    断言会引发某些异常，使用引发raise助手来断言某些代码引发异常
@version: 
'''


import pytest


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()