#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2021-05-02 13:06:05
lastTime: 2022-10-07 03:28:15
LastAuthor: Do not edit
FilePath: /Turing/test_demo.py
Description: 
version: 
'''

import pytest
# from test_demo2 import demo


l = ["First", "Second", "Third", "Fourth"]

# def setup_module(A):
#     test_demo().append(A)
        
@pytest.mark.parametrize('Num', l)
@pytest.mark.usefixtures('A')
def test_01(Num, A):
    print(Num, "---", A)

@pytest.mark.parametrize('case01, case02', [pytest.param('1', '2', id="X")])
def test_02(case01, case02):
    print(case01, case02)