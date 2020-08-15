#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2020-08-02 21:09:28
lastTime: 2020-08-02 23:19:38
LastAuthor: Do not edit
FilePath: \Turing\pytest_official\02.Usage and Invocations\test_example.py
@Description:
@version: 
'''

import pytest


@pytest.fixture
def error_fixture():
    assert 0  # 等同于: assert False


def test_ok():
    print("ok")


def test_fail():
    assert 0


def test_error(error_fixture):
    pass


def test_skip():
    pytest.skip("skipping this test")


def test_xfail():
    pytest.xfail("xfailing this test")


@pytest.mark.xfail(reason="always xfail")
def test_xpass():
    pass
