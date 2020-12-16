#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2020-11-29 16:50:36
lastTime: 2020-11-29 16:53:47
LastAuthor: Do not edit
FilePath: /Turing/pytest_official/testcases/pytest_dependency/test_basicUsage.py
Description: 
version: 
'''

import pytest

@pytest.mark.dependency()
@pytest.mark.xfail(reason='deliberate fail')
def test_a():
    assert False

@pytest.mark.dependency()
def test_b():
    pass

@pytest.mark.dependency(depends=['test_a'])
def test_c():
    pass

@pytest.mark.dependency(depends=['test_b'])
def test_d():
    pass

@pytest.mark.dependency(depends=['test_b', 'test_c'])
def test_e():
    pass

