#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pytest import ExitCode

'''
@Author: LEGEND
@since: 2020-08-01 21:59:19
lastTime: 2020-08-02 23:12:15
LastAuthor: Do not edit
FilePath: \Turing\pytest_official\02.Usage and Invocations\test_exitCodes.py
@Description: 
@version: 
'''
def func(x):
    # print(ExitCode)
    # print("\n退出码：{}".format(ExitCode.INTERNAL_ERROR))
    # print("\n退出码：{}".format(ExitCode.INTERRUPTED))
    # print("\n退出码：{}".format(ExitCode.NO_TESTS_COLLECTED))
    # print("\n退出码：{}".format(ExitCode.OK))
    # print("\n退出码：{}".format(ExitCode.TESTS_FAILED))
    # print("\n退出码：{}".format(ExitCode.USAGE_ERROR))
    # print("\n退出码：{}".format(ExitCode.as_integer_ratio))
    return x+1

def test_exitCodes():
    assert func(1) == 2
    
