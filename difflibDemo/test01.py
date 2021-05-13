#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2021-04-13 23:21:28
lastTime: 2021-05-11 22:50:15
LastAuthor: Do not edit
FilePath: /Turing/difflibDemo/test01.py
Description: 
    https://docs.python.org/zh-cn/3/library/difflib.html
    https://cloud.tencent.com/developer/article/1568500
    https://blog.csdn.net/IMW_MG/article/details/78149574
    https://www.programcreek.com/python/example/1084/difflib.Differ
version: 
'''

import difflib
from deepdiff import DeepDiff

text1='''1234567890
this is a text one.
heihiehie
'''
text1_line=text1.splitlines() #以行进行分割，以便以后对比

text2='''1234567890
this is a text two.
heihiehie
'''
text2_line=text2.splitlines()

d = difflib.Differ() #创建Differ()对象


# diff = d.compare(text1_line,text2_line).__sizeof__()
# print(diff)
# print('\n'.join(list(diff)))

print(DeepDiff(text1_line,text2_line, view='tree').get('two'))
# @pytest.mark.array_compare
# def test_succeeds():
