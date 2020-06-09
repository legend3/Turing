#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2020-06-07 20:08:24
@lastTime: 2020-06-09 22:42:02
@LastAuthor: Do not edit
@FilePath: \iPytest\testcase\all\test_01\test_mod_01.py
@Description: 
@version: 
'''


# test_mod_01.py

import pytest

@pytest.mark.dependency()
def test_a():
    pass

# @pytest.mark.dependency()
# @pytest.mark.xfail(reason="deliberate fail")
# def test_b():
#     assert False

@pytest.mark.dependency(depends=["test_a"])
def test_c():
    pass


# class TestClass(object):

#     @pytest.mark.dependency()
#     def test_b(self):
        # pass