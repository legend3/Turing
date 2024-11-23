#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2024-10-24 00:02:01
lastTime: 2024-10-24 00:14:32
LastAuthor: Do not edit
FilePath: /Python_Testing_with_pytest/pytest_order/Combination of absolute and relative ordering.py
Description: 如果将绝对顺序标记和相对顺序标记组合在一起，那么排序首先对绝对顺序标记(例如序数-index)进行，然后对相对顺序标记进行排序。这意味着相对排序总是具有优先性:
version: 
'''

import pytest

@pytest.mark.order(index=0, after="test_second")
def test_first():
    assert True

@pytest.mark.order(1)
def test_second():
    assert True


import pytest

@pytest.mark.order(after=["test_second"])
def test_first():
    assert True

@pytest.parametrize(param, [1, 2, 3])
def test_second(param):
    assert True