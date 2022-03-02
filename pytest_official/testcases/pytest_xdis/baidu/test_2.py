#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2022-03-03 01:15:34
lastTime: 2022-03-03 01:16:53
LastAuthor: Do not edit
FilePath: /Turing/pytest_official/testcases/pytest_xdis/baidu/test_2.py
Description: 
version: 
'''


import pytest
import time

def test_06(start, open_baidu):
    print("测试用例test_01")
    time.sleep(1)
    assert start == "yoyo"
def test_07(start, open_baidu):
    print("测试用例test_02")
    time.sleep(1)
    assert start == "yoyo"

if __name__ == "__main__":
    pytest.main(["-s", "test_2.py"])