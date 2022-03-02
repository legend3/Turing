#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2022-03-03 01:13:49
lastTime: 2022-03-03 01:17:14
LastAuthor: Do not edit
FilePath: /Turing/pytest_official/testcases/pytest_xdis/blog/conftest.py
Description: 
version: 
'''


import pytest

@pytest.fixture(scope="function")
def open_blog():
    print("打开blog页面_function")