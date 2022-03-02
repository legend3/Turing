#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2022-03-03 01:15:29
lastTime: 2022-03-03 02:26:30
LastAuthor: Do not edit
FilePath: /Turing/pytest_official/testcases/pytest_xdis/baidu/test_1_baidu.py
Description: 
version: 
'''


from multiprocessing import Process
import pytest
import time, os

@pytest.mark.parametrize('case', [1,2])
def test_01(start, open_baidu, case):
    print("测试用例test_01:{}".format(case))
    time.sleep(1)
    assert start == "yoyo"

@pytest.mark.parametrize('case', [1,2])
def test_02(start, open_baidu, case):
    time.sleep(5)
    print("测试用例test_02:{}".format(case))
    time.sleep(1)
    assert start == "yoyo"

if __name__ == "__main__":
    pytest.main(["-xvs", 
                    "pytest_official/testcases/pytest_xdis/baidu/test_1_baidu.py", 
                    "-n", "2"])
                    # , 
                    # "--alluredir", "/pytest_official/testcases/pytest_xdis/result"]
                    # )
    # 生成报告数据
    # os.system('allure generate -c -o {0} {1}'.format("pytest_official/testcases/pytest_xdis/report", "pytest_official/testcases/pytest_xdis/result"))
    # 展示报告
    # os.system('allure open {0}'.format("pytest_official/testcases/pytest_xdis/report"))