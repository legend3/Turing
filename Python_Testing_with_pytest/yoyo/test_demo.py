#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

'''
@Author: LEGEND
@since: 2020-06-17 01:37:14
@lastTime: 2020-06-17 02:28:37
@LastAuthor: Do not edit
@FilePath: \Turing\Pytest_learning\Python Testing with pytest\yoyo\test_demo.py
@Description: 
@version: 
'''
# from conftest import l
# print(l)

def test_getL(l):
    global l2
    l2 = l
    print(l2)


@pytest.mark.parametrize('data', l2)
def test_data(data):
    print(data)



