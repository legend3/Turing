#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

'''
@Author: LEGEND
@since: 2020-06-17 01:35:36
@lastTime: 2020-06-17 02:11:01
@LastAuthor: Do not edit
@FilePath: \Turing\Pytest_learning\Python Testing with pytest\yoyo\conftest.py
@Description: 
@version: 
'''



@pytest.fixture()
def l2():
    ll = [1,2,3]
    return ll

@pytest.fixture()
def l(l2):
    return l2