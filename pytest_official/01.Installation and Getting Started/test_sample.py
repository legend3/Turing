#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pytest import ExitCode
'''
@Author: LEGEND
@since: 2020-08-01 20:50:20
@lastTime: 2020-08-01 22:10:16
@LastAuthor: Do not edit
@FilePath: \Turing\Python_Testing_with_pytest\pytest_official\01.Installation and Getting Started\test_sample.py
@Description: 第一个pytest测试
    1.现在可以在命令行中使用pytest命令执行测试方法
    2.[50%]、[100％]是指运行所有测试用例的总体进度
    3.您可以使用assert语句来验证测试期望。 
    pytest的Advanced assertion introspection将智能地报告assert表达式的中间值，因此您可以避免使用许多JUnit传统方法的名称。
    4.运行多个测试
    pytest将运行所有格式为test*.py或*_测试.py在当前目录及其子目录中。更一般地说，它遵循标准的测试发现规则。
@version: 
'''


def func(x):
    print("退出码：{}".format(ExitCode.INTERNAL_ERROR))
    return x + 1


def test_answer():
    assert func(3) == 4

def test_answer2():
    assert func(2) == 3
