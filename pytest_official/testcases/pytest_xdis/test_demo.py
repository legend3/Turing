#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2022-03-03 02:32:36
lastTime: 2022-03-03 03:12:35
LastAuthor: Do not edit
FilePath: /Turing/pytest_official/testcases/pytest_xdis/test_demo.py
Description: 
version: pytest-xdist==2.5
'''
import pytest

@pytest.mark.xdist_group(name="group1")  # 关联：--dist=loadgroup   这保证了具有相同xdist_group名称的所有测试都在同一个工作进程中运行。
def test1():
    pass

class TestA:
    @pytest.mark.xdist_group("group1")
    @pytest.mark.parametrize('case', [1,2])
    def test2(self, case):
        pass

if __name__ == "__main__":
    pytest.main(["-xvs", 
                    "-n", "2", # 指定进程数
                    # "--maxprocesses=1", # 限制进程数
                    # "--dist=loadgroup",
                    "pytest_official/testcases/pytest_xdis/test_demo.py"
                    ])