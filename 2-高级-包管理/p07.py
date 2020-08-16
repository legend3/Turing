#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2019-12-22 11:35:22
lastTime: 2020-08-16 23:15:59
FilePath: \Turing\2-高级-包管理\p07.py
@Description: 
@version: 
'''


# 直接导入一个包，可以使用__init__.py中的内容
# import pkg01
# pkg01.inInit()


# 此种方法是默认对__init__.py内容的导入
import pkg01 as pp
pp.inInit()
