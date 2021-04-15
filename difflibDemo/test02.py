#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2021-04-13 23:38:20
lastTime: 2021-04-13 23:41:35
LastAuthor: Do not edit
FilePath: /Turing/difflibDemo/test02.py
Description: 
version: 
'''

import difflib

text1='''1234567890
this is a text one.
heihiehie
'''

text1_line=text1.splitlines() #以行进行分割，以便以后对比

text2='''235678956545
This is a Text two.
heiheihei
'''

text2_line=text2.splitlines()
d = difflib.HtmlDiff() #创建Differ()对象
print(d.make_file(text1_line,text2_line))

# 执行命令生成html: python test02.py >> diff.html