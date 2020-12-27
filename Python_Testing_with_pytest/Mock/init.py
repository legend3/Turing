#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2020-12-26 15:42:42
lastTime: 2020-12-27 11:40:48
LastAuthor: Do not edit
FilePath: /Turing/Python_Testing_with_pytest/Mock/init.py
Description: 
            init是mock对象的构造器，
            name是mock对象的唯一标识；
            spec设置的是mock对象的属性，可以是property或者方法，也可以是其他的列表字符串或者其他的python类；
            return_value设置的是，当这个mock对象被调用的时候，显示出的结果就是return_value的值；
            side_effect是和return_value是相反的，覆盖了return_value，也就是说当这个mock对象被调用的时候，返回的是side_effect的值，而不是return_value。
version: 
'''

""" name """
from unittest.mock import Mock
mockObj = Mock(name='foo')  # 模拟出一个属性为foo的Mock
print(mockObj)  # <Mock name='foo' id='2438327763392'>name标识了唯一的一个mock（print的时候，后边会显示ID）
# print(repr(mockObj))  # 将对象转化为供解释器读取的形式

""" return_value """
mockFoo = Mock(return_value=100)  # 1.定义了一个Mock对象，2.设置了Mock类的返回值（a.指定的是某个值：）
print(mockFoo)  # <Mock id='1248682934432'>
print(mockFoo())  # 100，从上边的例子可以看出，当我们调用mock对象的时候，显示的就是return_value的值（也就是说mockObj是带有一定的功能的）

class Foo(object):
    _num = 100
    def fun1(self):
        print('call fun1')
    
    def fun2(self, argsValue):
        print("value=", argsValue)

fooObj = Foo()
print(fooObj)

mockFoo = Mock(return_value=fooObj)
print(mockFoo)
mockObj = mockFoo()
print(mockObj)
print(mockObj._num)
print(mockObj.fun1())


""" getvalue """