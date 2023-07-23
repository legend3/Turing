#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2019-12-22 11:35:22
lastTime: 2023-04-08 18:27:11
LastAuthor: Do not edit
FilePath: /Turing/13-协程/v01.py
Description: 
version: 
'''

def simple_coroutine(): # 生成器
    print('-> start')
    x = yield
    print('-> recived', x)

sc = simple_coroutine()
print(1)
# 可以使用sc.send(None)，效果一样
next(sc)

print(2)
sc.send('zhexiao')
