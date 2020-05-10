#!/usr/bin/env python
# -*- coding: utf-8 -*-

import importlib
import os
import sys

'''
@Author: LEGEND
@since: 2020-05-11 01:54:03
@lastTime: 2020-05-11 04:21:28
@FilePath: \Turing\2-高级-包管理\rootTest.py
@Description: 
@version: 
'''



# curPath = os.path.abspath(__file__)
# rootPath = os.path.split(curPath)[0] + '/../'
# print(os.path.abspath(rootPath))

# print(os.path.dirname(curPath))  #
# sys.path.append(os.path.dirname(curPath))

# reload(sys)  # 用于重新载入之前载入的模块。(载入过在sys.path中加入过'python基础',sys.path中就一直存在'python基础'包模块)
# sys.setdefaultencoding('utf-8')  # # 设置编码
# sys.path.append(sys.path[0] + "/../")
sys.path.append(os.path.abspath(sys.path[0] + "/../"))
# print("这里", os.path.abspath(sys.path[0] + "/../"))

# sys.path.append(os.getcwd())  # 获取的是工作空间的路径

# s = importlib.import_module('.01','2-高级-包管理')
s = importlib.import_module('2-高级-包管理.01')
                                                # params = importlib.import_module('b.c.c') #绝对导入
                                                # params_ = importlib.import_module('.c.c',package='b') #相对导入

                                                # # 对象中取出需要的对象
                                                # params.args #取出变量
                                                # params.C  #取出class C
                                                # params.C.c  #取出class C 中的c 方法


s.Student()

# from i import p01
# tuling.Student()


