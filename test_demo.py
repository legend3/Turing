#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2021-05-02 13:06:05
lastTime: 2024-04-25 00:46:51
LastAuthor: Do not edit
FilePath: /Turing/test_demo.py
Description: 
version: 
'''

import pytest
# from test_demo2 import demo


# l = ["First", "Second", "Third", "Fourth"]

# def setup_module(A):
#     test_demo().append(A)
        
# @pytest.mark.parametrize('Num', l)
# @pytest.mark.usefixtures('A')
# def test_01(Num, A):
#     print(Num, "---", A)

# @pytest.mark.parametrize('case01, case02', [pytest.param('1', '2', id="X")])
# def test_02(case01, case02):
#     print(case01, case02)


import pytest

@pytest.fixture
def data_01(request):
    if request.node.get_closest_marker("skip"):
        pytest.skip("skip 01")
    return None  # 返回 None 确保后续 fixture 和测试函数继续执行

@pytest.fixture
def data_02(request, data_01):
    print("02")

def test(data_02):
    print('ok')







# # 定义一个额外的 fixture，在 data_01 fixture 被跳过时调用
# @pytest.fixture
# def continue_execution():
#     yield
#     # 在此处添加后续 fixture 和测试函数的调用

# @pytest.fixture
# def data_01():
#     pytest.skip("skip 01")

# @pytest.fixture
# def data_02(request, data_01):
#     print("02")

# def test(data_02, continue_execution):
#     print('ok')

if __name__ == '__main__':
    from datetime import datetime
    from icecream import ic 
    import time
    from datetime import datetime

    def time_format():
        return f'{datetime.now()}|> '

    ic.configureOutput(prefix=time_format)

    for _ in range(3):
        time.sleep(1)
        ic('Hello')

