#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2019-12-22 11:35:22
@lastTime: 2020-05-11 03:09:49
@FilePath: \Turing\2-高级-包管理\p10.py
@Description: 
@version: 
'''





import os
import sys
import importlib
curPath = os.path.abspath(__file__)
parentPath = os.path.dirname(curPath)
sys.path.append(parentPath)

from pkg02 import *
from python基础 import *

# inInit()  # （此时）因为__init__.py中增添了__all__=['p01']，所以按照`__all__` 指定的子包或者模块进行加载，则不会载入`__init__`中的内容

stu = p01.Student()
stu.say()

p01.sayHello()

# stu2 = p02.Student2()
# stu2.say()
