#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2024-06-13 00:25:08
lastTime: 2024-06-13 00:25:58
LastAuthor: Do not edit
FilePath: /Turing/Design_Model/Chapter20/TextBox.py
Description: 
version: 
'''





from abc import ABC, abstractmethod

""" 具体中介者 """
class TextBox(ABC):
    # 维持对各个同时对象的引用
    