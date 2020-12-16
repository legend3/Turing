#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2020-11-30 01:51:47
lastTime: 2020-11-30 02:18:07
LastAuthor: Do not edit
FilePath: /Turing/pytest_official/testcases/pytest_dependency/test.py
Description: 
version: 
'''
import pytest

@pytest.mark.parametrize('data', [1,2,3])
def test_01(data, request):
    print(request.params)
