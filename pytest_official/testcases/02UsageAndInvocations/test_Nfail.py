#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2020-08-01 21:59:19
@lastTime: 2020-08-02 00:01:46
@LastAuthor: Do not edit
@FilePath: \Turing\Python_Testing_with_pytest\pytest_official\02.Usage and Invocations\test_Nfail.py
@Description: pytest测试过程中在第一个（或N个）故障后停止
    pytest -x＃第一次失败后停止
    pytest --maxfail = 2＃两次失败后停止
@version: 
'''
def func(x):
    return x+1

def test_firstfail():
    a = 3
    assert func(1) == a
    
def test_Nfail():
    a = 2
    assert func(1) == a
    
