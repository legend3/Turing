#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2022-03-03 01:15:53
lastTime: 2022-03-03 01:17:28
LastAuthor: Do not edit
FilePath: /Turing/pytest_official/testcases/pytest_xdis/blog/test_2_blog.py
Description: 
version: 
'''



import pytest
import time
def test_03(start, open_blog):
    print("测试用例test_03")
    time.sleep(1)
    assert start == "yoyo"

def test_04(start, open_blog):
    print("测试用例test_04")
    time.sleep(1)
    assert start == "yoyo"

def test_05(start, open_blog):
    '''跨模块调用baidu模块下的conftest'''
    print("测试用例test_05,跨模块调用baidu")
    time.sleep(1)
    assert start == "yoyo"

if __name__ == "__main__":
    pytest.main(["-s", "test_2_blog.py"])