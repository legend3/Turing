#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2020-12-26 14:09:51
lastTime: 2020-12-26 14:32:11
LastAuthor: Do not edit
FilePath: /Turing/Python_Testing_with_pytest/Mock/quickguide.py
Description: 
version: 
'''


from unittest.mock import MagicMock


class ProductionClass(object):
    """
    docstring
    """
    pass


thing = ProductionClass()
thing.method = MagicMock(return_value=3)  # 通过MagicMock给ProductionClass的实例定义方法的返回值
thing.method(3, 4, 5, key='value')  # 通过MagicMock给ProductionClass的实例定义方法的限制可访问属性
thing.method.assert_called_with(3, 4, key='value')