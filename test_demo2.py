#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2021-05-02 13:08:27
lastTime: 2021-05-03 01:27:49
LastAuthor: Do not edit
FilePath: /Turing/test_demo2.py
Description: 
version: 
'''
import unittest

r = []

def test_01(A):
    global r
    r.append('A')
    print(r)
    # return f

@test_01
def test_02(args):
    print(args)
    
# test_02(r)