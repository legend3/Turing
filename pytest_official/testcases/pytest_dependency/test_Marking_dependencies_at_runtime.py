#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2020-11-30 01:44:24
lastTime: 2020-11-30 09:34:24
LastAuthor: Do not edit
FilePath: /Turing/pytest_official/testcases/pytest_dependency/test_Marking_dependencies_at_runtime.py
Description: 
version: 
'''


import pytest
from pytest_dependency import depends

@pytest.mark.dependency()
def test_a():
    pass

@pytest.mark.dependency()
@pytest.mark.xfail(reason="deliberate fail")
def test_b():
    assert False

@pytest.mark.dependency()
def test_c(request):
    depends(request, ["test_b"])
    pass

@pytest.mark.dependency()
def test_d(request):
    depends(request, ["test_a"])
    pass