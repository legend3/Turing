#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2020-06-23 22:32:08
@lastTime: 2020-06-24 00:11:16
@LastAuthor: Do not edit
@FilePath: \Turing\Design_Model\Chapter02\1.2object_type_function.py
@Description: 
@version: 
'''

# 多态
a = "John"
b = (1,2,3)
c = [3,4,6,8,9]
print(a[1], b[0], c[2])


# 继承
class A(object):
    def a1(self):
        print("a1")
    
class B(A):
    def b(self):
        print("b")
b = B()
b.a1()

# 组合
class A(object):
    def a1(self):
        print("a1")
    
class B(object):
    def b(self):
        print("b")
        A().a1()  # A是引用，A()是实例；实例引用方法

objectbB = B()
objectbB.b()