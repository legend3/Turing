#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2019-12-22 11:35:22
@lastTime: 2020-05-04 17:12:50
@FilePath: \Turing\2-高级-包管理\p01.py
@Description: 
@version: 
'''



# 包含一个学生类，
# 一个sayhello函数，
# 一个打印语句


class Student():
    def __init__(self, name="initSay", age=18):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0}".format(self.name))


def sayHello():
    print("Hi, 欢迎来到图灵学院！")


print("print会随模块或者main方法自动输出")  # 

# 此判断语句建议一直作为程序的入口
if __name__ == '__main__':
    print("我是模块p01呀，你特么的叫我干毛")
