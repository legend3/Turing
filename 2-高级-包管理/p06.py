#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2019-12-22 11:35:22
@lastTime: 2020-04-30 01:23:12
@FilePath: \Turing\2-高级-包管理\p06.py
@Description: 
@version: 
'''


# 系统默认的模块搜索路径
import sys

print(type(sys.path))
print(sys.path)  # 属性可以获取路径列表

for p in sys.path:  # 遍历路径列表
    print(p)
