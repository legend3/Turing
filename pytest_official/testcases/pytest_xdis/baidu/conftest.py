#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2022-03-03 01:13:49
lastTime: 2022-03-03 01:17:42
LastAuthor: Do not edit
FilePath: /Turing/pytest_official/testcases/pytest_xdis/baidu/conftest.py
Description: 
version: 
'''

import pytest

@pytest.fixture(scope="session")
def open_baidu():
    print("打开百度页面_session")
