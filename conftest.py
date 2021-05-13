#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2021-05-02 13:03:09
lastTime: 2021-05-02 13:24:52
LastAuthor: Do not edit
FilePath: /Turing/conftest.py
Description: 
version: 
'''
import pytest


@pytest.fixture()
def A():
    return 'A'

@pytest.fixture()
def B():
    return 'B'
