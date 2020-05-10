#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2019-12-22 11:35:22
@lastTime: 2020-05-04 16:38:22
@FilePath: \Turing\9-调试\01.py
@Description: 
@version: 
'''



def SayHello(name):
    print("I want to say hello with your, {0}".format(name))
    print("Hello, {0}".format(name))
    print("Done...............")


if __name__ == "__main__":
    print('***' * 10)
    name = input("Please input your name: ")
    print(SayHello(name=name) )
    print('@@@' * 10)
    # æµ‹è¯•æ¡ˆä¾‹