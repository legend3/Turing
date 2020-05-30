#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2020-05-27 23:49:03
@lastTime: 2020-05-28 00:24:24
@FilePath: \Turing\Pytest_learning\Python Testing with pytest\hook\test_wrapper.py
@Description: 
@version: 
'''


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    print(outcome.get_result())
    

def test_a(pytest_runtest_makereport):
    print("成功！")