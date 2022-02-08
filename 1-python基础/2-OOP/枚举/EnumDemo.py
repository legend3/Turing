#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2020-08-01 20:07:26
lastTime: 2022-02-08 18:03:48
LastAuthor: Do not edit
FilePath: /Turing/1-python基础/2-OOP/枚举/EnumDemo.py
@Description: 
@version: 
'''

# # 使用普通类直接实现枚举
# #   在Python中，枚举和我们在对象中定义的类变量时一样的，每一个类变量就是一个枚举项，访问枚举项的方式为：类名加上类变量，像下面这样：
# class color():
#     YELLOW  = 1
#     RED     = 2
#     GREEN   = 3
#     PINK    = 4
 
# # 访问枚举项
# print(color.YELLOW) # 1
# # 　　虽然这样是可以解决问题的，但是并不严谨，也不怎么安全，比如：
# # 　　1、枚举类中，不应该存在key相同的枚举项（类变量）
# # 　　2、不允许在类外直接修改枚举项的值

# class color():
#     YELLOW  = 1
#     YELLOW  = 3   # 注意这里又将YELLOW赋值为3，会覆盖前面的1
#     RED     = 2
#     GREEN   = 3
#     PINK    = 4
 
# # 访问枚举项
# print(color.YELLOW) # 3
 
# # 但是可以在外部修改定义的枚举项的值，这是不应该发生的
# color.YELLOW = 99
# print(color.YELLOW) # 99

# # 解决方案：使用enum模块
# # 　　enum模块是系统内置模块，可以直接使用import导入，但是在导入的时候，不建议使用import enum将enum模块中的所有数据都导入，一般使用的最多的就是enum模块中的Enum、IntEnum、unique这几项

# # 导入枚举类
# from enum import Enum
 
# # 继承枚举类
# class color(Enum):
#     YELLOW  = 1
#     BEOWN   = 1 
#     # 注意BROWN的值和YELLOW的值相同，这是允许的，此时的BROWN相当于YELLOW的别名
#     RED     = 2
#     GREEN   = 3
#     PINK    = 4
 
# class color2(Enum):
#     YELLOW  = 1
#     RED     = 2
#     GREEN   = 3
#     PINK    = 4
# # 　　使用自己定义的枚举类：

# print(color.YELLOW) # color.YELLOW
# print(color.BEOWN) # color.YELLOW
# print(type(color.YELLOW)) # <enum 'color'>
 
# print(color.YELLOW.value)  # 1
# print(type(color.YELLOW.value)) # <class 'int'>

# print(color.YELLOW == 1)    # False
# print(color.YELLOW.value == 1)  # True
# print(color.YELLOW == color.YELLOW)  # True
# print(color.YELLOW == color2.YELLOW)  # False
# print(color.YELLOW is color2.YELLOW)  # False
# print(color.YELLOW is color.YELLOW)  # True
 
# print(color(1))         # color.YELLOW
# print(type(color(1)))   # <enum 'color'>
# # 注意事项如下：
# # 1、枚举类不能用来实例化对象
# # 2、访问枚举类中的某一项，直接使用类名访问加上要访问的项即可，比如 color.YELLOW
# # 3、枚举类里面定义的Key = Value，在类外部不能修改Value值，也就是说下面这个做法是错误的
#     # 修改枚举值
#     # color.YELLOW = 2  # Wrong, can't reassign member
# # 4、枚举项可以用来比较，使用==，或者is
# # 5、导入Enum之后，一个枚举类中的Key和Value，Key不能相同，Value可以相同，但是Value相同的各项Key都会当做别名，
# # *6、如果要枚举类中的Value只能是整型数字，那么，可以导入IntEnum，然后继承IntEnum即可，注意，此时，如果value为字符串的数字，也不会报错：(不会！)
#     # 指定枚举值的数据类型
# from enum import IntEnum
# class color3(IntEnum):
#     YELLOW  = "1"
# print(color3.YELLOW.value)
# # 7、如果要枚举类中的key也不能相同，那么在导入Enum的同时，需要导入unique函数
# from enum import Enum, unique
# @unique
# class color4(Enum):
#     YELLOW  = 1
#     GREEN  = 1
# print(color4.YELLOW.value)




# 什么是枚举类？
    # 对象有限且固定的类；（比如季节类，只包括春夏秋冬四个对象）

# 1. 两种方式定义枚举类
    # 1）直接使用Enum()函数列出多个枚举值来创建枚举类；
# from enum import Enum
# # 定义Season枚举类
# Season = Enum('Season', ('SPRING', 'SUMMER', 'FALL', 'WINTER'))
# # 第一个参数值为枚举类的类名，第二个参数值为一个元组，用于列出所有的枚举对象

# # 测试枚举对象两个属性的用法
# print(Season.SPRING)        # Season.SPRING
# print(Season.SUMMER.name)   # SUMMER
# print(Season.FALL.value)    # 3

# # 程序可以通过枚举对象名或者枚举对象序号值访问枚举对象：
# print(Season['SPRING'])     # Season.SPRING
# print(Season(2))            # Season.SUMMER  注意是括号

# # python还为枚举提供了一个__members__属性，该属性返回一个dict字典，字典包含所有的枚举对象：
# print(Season.__members__)
# # OrderedDict([('SPRING', <Season.SPRING: 1>), ('SUMMER', <Season.SUMMER: 2>), ('FALL', <Season.FALL: 3>), ('WINTER', <Season.WINTER: 4>)])
 
# print(Season.__members__.items())
# # odict_items([('SPRING', <Season.SPRING: 1>), ('SUMMER', <Season.SUMMER: 2>), ('FALL', <Season.FALL: 3>), ('WINTER', <Season.WINTER: 4>)])

# # 为对象新建实例变量或者方法，枚举对象用“ 类名.对象名 ”表示：
# Season.SPRING.day = 31+28+31
# print(Season.SPRING.day)        # 90
 
# def inf():
#     print("春天")    
# Season.SPRING.des = inf
# Season.SPRING.des()             # 春天

    # 2）通过继承Enum类定义枚举类（可以定义自己的方法）
# from enum import Enum
# class Season(Enum):
#     # 创建枚举对象并指定value值
#     SPRING = "1"
#     SUMMER = "2"
#     FALL = "3"
#     WINTER = "4"
#     def inf(self):
#         if self.value == '1':
#             print("春天")
#         elif self.value == '2':
#             print("夏天")
#         elif self.value == '3':
#             print("秋天")
#         else:
#             print("冬天")
# print(Season.SPRING)            # Season.SPRING
# print(Season.SPRING.name)       # SPRING
# print(Season.SPRING.value)      # 1   这个1是字符串类型
# print(Season['SPRING'])         # Season.SPRING
# Season.SPRING.inf()             # Season.SPRING

# 2. 枚举类定义构造函数
from enum import Enum
class Season(Enum):
    # 创建枚举对象并指定value值，超过一个值Python会自动将其封装成一个元组传给value
    SPRING = "1", "春天"
    SUMMER = "2", "夏天"
    FALL = "3", "秋天"
    WINTER = "4", "冬天"
    
    # 因为枚举类对象已经确定，所以构造函数不会用于创建新对象，其主要作用是映射对象的value值，
    # value值有几个元素，构造函数就有几个参数（不包括参数self）
    def __init__(self, num, ch_name):
        self.num = num
        self.ch_name = ch_name
 
# value值以元组形式输出
print(Season.SPRING.value)      # ('1', '春天')
 
# num、ch_name分别映射value元组的每个元素
print(Season.SPRING.num)
print(Season.SPRING.ch_name)