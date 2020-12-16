#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2020-11-30 01:20:43
lastTime: 2020-11-30 01:42:26
LastAuthor: Do not edit
FilePath: /Turing/pytest_official/testcases/pytest_dependency/test_Using_test_classes.py
Description: 在类中使用标记名命被依赖是不被支持的
version: 
'''


import pytest


class TestClass(object):

    @pytest.mark.dependency()
    @pytest.mark.xfail(reason="deliberate fail")
    def test_a(self):
        assert False

    @pytest.mark.dependency()
    def test_b(self):
        pass

    @pytest.mark.dependency(depends=["TestClass::test_a"])
    def test_c(self):
        pass

    @pytest.mark.dependency(depends=["TestClass::test_b"])
    def test_d(self):
        pass

    @pytest.mark.dependency(depends=["TestClass::test_b", "TestClass::test_c"])
    def test_e(self):
        pass


class TestClassNamed(object):

    @pytest.mark.dependency(name="a")
    @pytest.mark.xfail(reason="deliberate fail")
    def test_a(self):
        assert False

    @pytest.mark.dependency(name="b")
    def test_b(self):
        pass

    @pytest.mark.dependency(name="c", depends=["a"])
    def test_c(self):
        pass

    @pytest.mark.dependency(name="d", depends=["b"])
    def test_d(self):
        pass

    @pytest.mark.dependency(name="e", depends=["b", "c"])
    def test_e(self):
        pass