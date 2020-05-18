#!/usr/bin/env python
# -*- coding: utf-8 -*-

import importlib
import os
import sys

'''
@Author: LEGEND
@since: 2020-05-11 01:54:03
@lastTime: 2020-05-19 02:50:37
@FilePath: \Turing\2-高级-包管理\rootTest.py
@Description: (不)同级包之间的导包
@version: 
'''

if __name__ == '__main__':

    # params = importlib.import_module('b.c.c') #绝对导入
    # params_ = importlib.import_module('.c.c',package='b') #相对导入

    # # 对象中取出需要的对象
    # params.args #取出变量
    # params.C  #取出class C
    # params.C.c  #取出class C 中的c 方法

    """
    说明：(pydev在运行时会把当前工程的所有文件夹路径都作为包的搜索路径)，而命令行默认只是搜索当前路径(和系统包，没有项目工程目录路径！)。
    sys.path中增加Turning项目，就能自由导入Turning中的包、模块使用
    """
    # importlib.reload(sys)  # (永久)用于重新载入之前载入的模块。(载入过在sys.path中加入过'python基础',sys.path中就一直存在'python基础'包模块)
    # sys.getdefaultencoding()  # 获悉设置编码
    # print(sys.path)

    """第一种方式"""
    print(os.getcwd())  # 查看当前项目目录
    curPath = os.path.abspath(__file__)  # 查看当前文件路径
    print(curPath)
    rootPath = os.path.split(curPath)[0] # + '/../' # 文件目录所在路径
    print(os.path.abspath(rootPath))  # 设置项目根路径
    sys.path.append(rootPath)

    # print(os.path.dirname(curPath))
    # print(sys.path)

    # """第二种方式"""
    # # sys.path.append(os.getcwd())  # 获取当前目录
    # # print(os.path.abspath(__file__))
    # print(os.getcwd())  # 获取当前目录
    # # print(os.path.abspath(os.path.join(os.getcwd(),"..")))  # 上一级目录
    # # print(os.path.abspath(os.path.join(os.getcwd(), "../..")))  # 上上级目录

    # from pythonTest import test
    # test.Student()


    # s = importlib.import_module('.01','1-python基础.2-OOP')
    s = importlib.import_module('1-python基础.2-OOP.01')

    s.Student()

