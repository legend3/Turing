#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import os

'''
@Author: LEGEND
@since: 2020-06-03 00:18:57
@lastTime: 2020-07-03 03:23:32
@FilePath: \Turing\Pytest_learning\Python Testing with pytest\yoyo\allure\testfix.py
@Description: 
@version: 
'''


# 函数式
def setup_function():
    print("setup_function：每个用例开始前都会执行")


def teardown_function():
    print("teardown_function：每个用例结束后都会执行")


def test_one():
    print("正在执行----test_one")
    x = "this"
    assert 'h' in x


# def test_two():
#     print("正在执行----test_two")
#     x = "hello"
#     assert hasattr(x, 'check')


# def test_three():
#     print("正在执行----test_three")
#     a = "hello"
#     b = "hello world"
#     assert a in b


if __name__ == "__main__":
    pytest.main(['-vs', os.path.abspath(__file__)])  # os.path.abspath(__file__)
