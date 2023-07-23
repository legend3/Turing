#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2019-12-22 11:35:21
lastTime: 2022-08-08 00:59:59
FilePath: /Turing/1-python基础/2-OOP/01.py
@Description: 
@version: 
'''

'''
    定以一个学生类，用来形容学生
'''

# 定义一个空的类
class Student():
    # 一个空类，pass代表直接跳过
    # 此处pass必须有
    pass

# 定义一个对象
mingyue = Student()

# 再定义一个类，用来描述听Python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None 
    # 补充：静态变量：1.用通过类名或对象实例访问静态变量都是合法的 
                 # 2.必须通过类型访问才能修改静态变量的值（可以用id()查看静态变量id验证！）
    age = 18
    course = "Python"

    # 需要注意
    # 1. def doHomework的缩进层级
    # 2. 系统默认由一个self参数
    def doHomework(self):
        print("I 在做作业")

        # 推荐在函数末尾使用return语句
        return None

# 实例化一个叫yueyue的学生，是一个具体的人
yueyue = PythonStudent()
print(yueyue.name)  # 补充：用类实例访问静态变量
print(yueyue.age)
# 注意成员函数的调用没有传递进入参数
yueyue.doHomework()
PythonStudent.name  # 补充：通过类名访问静态变量
