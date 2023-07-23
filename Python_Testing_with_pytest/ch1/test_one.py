#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2020-03-22 04:32:39
lastTime: 2022-10-07 03:48:24
LastAuthor: Do not edit
FilePath: /Turing/Python_Testing_with_pytest/ch1/test_one.py
Description: 
version: 
'''

#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import pytest


def test_passing():
    assert (1, 2, 3) == (1, 2, 3)  # 断言
