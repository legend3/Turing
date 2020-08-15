#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2020-06-23 22:32:08
@lastTime: 2020-06-23 22:39:54
@LastAuthor: Do not edit
@FilePath: \Turing\Design_Model\Chapter01\object_type_function.py
@Description: 
@version: 
'''


class Person(object):
    '''
    @description: 
        1.类可以定义对象的属性和行为
        2.类包含了构造方法，构造方法的作用是为对象提供初始状态
        3.类就像模板一样，非常易于重复使用
    @param {type} 
    @return: 
    '''
    def __init__(self, name, age):
        self.name = name  # 数据成员/属性
        self.age =  age
    
    def get_person(self, ):  # 成员方法
        '''
        @description: 
            1.方法表示对象的行为
            2.方法可以对属性进行处理，从而实现所需的功能
        @param {type} 
        @return: 
        '''
        return "<Person (%s, %s)>" % (self.name, self.age)
    
p = Person("John", 32)  #  p是Person类的对象；
                        # 1.对象表示所开发的应用程序内的实体
                        # 2.实体之间可以通过交互来解决现实世界的问题
                        # 例如，Person是实体，而Car也是实体。Person可以驾驶Car，从一个地方开到另一个地方。
print("对象的类型：", type(p), "内存地址：", id(p))
