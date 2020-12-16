#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2020-11-29 16:59:55
lastTime: 2020-11-29 17:04:11
LastAuthor: Do not edit
FilePath: /Turing/pytest_official/testcases/pytest_dependency/test_namingtests.py
Description: 给被依赖项目取名字(默认省略值是函数的node ID);这样就不用写被依赖项的全称
version: 
'''
import pytest

@pytest.mark.dependency(name="a")
@pytest.mark.xfail(reason="deliberate fail")
def test_a():
    assert False
@pytest.mark.dependency(name="b")
def test_b():
    pass
@pytest.mark.dependency(name="c", depends=["a"])
def test_c():
    pass
@pytest.mark.dependency(name="d", depends=["b"])
def test_d():
    pass
@pytest.mark.dependency(name="e", depends=["b", "c"])
def test_e():
    pass
