#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2019-12-22 11:35:22
lastTime: 2020-08-17 02:07:02
FilePath: \Turing\2-高级-包管理\p08.py
@Description: 
@version: 
'''


'''
    导入包及包中模块
'''
import pkg01.p01  # （包和模块都会可以被执行）最先执行p01中的输出    "我是模块p01呀，你特么的叫我干毛"

pkg01.inInit()  # 后于模块的print输出

stu = pkg01.p01.Student()
stu.say()

pkg01.p01.sayHello()

