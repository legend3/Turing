#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2020-06-06 16:17:05
lastTime: 2022-08-09 13:05:35
FilePath: /Turing/14-Spider/v23.py
@Description: 
@version: 
'''


'''
python中正则模块是re
使用大致步骤：
1. compile函数将正则表达式的字符串编译为一个Pattern对象
2. 通过Pattern对象的一些列方法(方法先会将要匹配的字符串转换为正则表达式对象)对文本进行匹配，匹配结果是一个Match对象
3. 用Match对象的方法，对结果进行操纵

'''


import re

# \d表示以数字
# 后面+号表示这个数字可以出现一次或者多次
# s = r"\d+" # r表示后面是原生字符串，后面不需要转义


# 返回Pattern对象
# pattern = re.compile(s)
pattern = re.compile(r'\d+')  # complie将正则表达式编译成一个Pattern对象

# 返回一个Match对象
# 默认找到一个匹配就返回
m = pattern.match("one12two2three3")

print(type(m))
# 默认匹配从头部开始匹配，所以此次结果为None

print(m)
# 因为m没有匹配到任何结果，所以m.group()会报错
# print(m.group())

# 返回一个Match对象
# 后面为位置参数含义是从哪个位置开始查找，找到哪个位置结束
m = pattern.match("one12two2three3", 3, 10)

print(type(m))
# 默认匹配从头部开始，所以此次结果为None
print(m)


print(m.group())
# print(m.start(0))
# print(m.end(0))
# print(m.span(0))


# . * ?
s1 = [r"ab.*",r"ab.*?",r"abc."]
for i in s1:
    # pattern = re.compile(i)
    print(i)
    