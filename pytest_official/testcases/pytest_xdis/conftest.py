#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2022-03-03 01:13:49
lastTime: 2022-03-03 01:20:36
LastAuthor: Do not edit
FilePath: /Turing/pytest_official/testcases/pytest_xdis/conftest.py
Description: 
version: 
'''


import pytest

@pytest.fixture(scope="session")
def start():
    print("\n打开首页")
    return "yoyo"
