#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2021-05-02 13:06:05
lastTime: 2021-05-03 01:31:50
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
    print(A)
