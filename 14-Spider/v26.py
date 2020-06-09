#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author: LEGEND
@since: 2019-12-22 11:35:22
@lastTime: 2020-06-06 15:56:19
@FilePath: \Turing\14-Spider\v26.py
@Description:
@version:
"""


'''
findall??
'''
import re

pattern = re.compile(r'\d+')

s = pattern.findall("i am 18 years old and 185 high")

print(s)

s = pattern.finditer("i am 18 years old and 185 high")
print(type(s))
for i in s:
    print(i.group(0))
