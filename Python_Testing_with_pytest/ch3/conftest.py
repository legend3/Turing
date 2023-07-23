#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2022-10-07 03:36:15
lastTime: 2022-10-07 04:10:01
LastAuthor: Do not edit
FilePath: /Turing/Python_Testing_with_pytest/ch3/conftest.py
Description: 
version: 
'''

import pytest

@pytest.fixture(scope='session')
def anything():
    print('anything.')
    return 'anything'