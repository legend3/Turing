#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

'''
@Author: LEGEND
@since: 2020-06-14 18:22:28
@lastTime: 2020-06-14 19:02:13
@LastAuthor: Do not edit
@FilePath: \Turing\Pytest_learning\Python Testing with pytest\ch2\tasks_proj\tests\func\test_p.py
@Description: 
@version: 
'''


l = ("a", "b", "c")
l2 = ("d", "e", "f")

lid = [1, 2, 3]
ids = [i for i in lid]


@pytest.fixture(params=l, ids=ids)
def test_a(request):
    return request.param


@pytest.mark.parametrize('l2', l2,ids=ids)
def test_b(l2, test_a):
    print("l2参数：", l2)

