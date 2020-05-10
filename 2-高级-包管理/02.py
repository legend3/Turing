#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2019-12-22 11:35:22
@lastTime: 2020-05-11 03:30:58
@FilePath: \Turing\2-高级-包管理\02.py
@Description: 以整个模块为单位
@version: 
'''


# 借助于importlib包可以实现导入以数字开头的模块名称
import importlib
tuling = importlib.import_module("01")  # 相当于导入了一个叫01的模块并把导入模块赋值给了tuling

stu = tuling.Student()
stu.say()
tuling.sayHello()