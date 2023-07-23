#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2022-08-06 22:38:16
lastTime: 2022-08-06 22:40:54
LastAuthor: Do not edit
FilePath: /Turing/Deepdiff/test_01.py
Description: 
version: 
'''

from pprint import pprint
from deepdiff import DeepDiff

def test_case_01():
    a = "Object01"
    b = "Object"
    pprint(DeepDiff(a, b))
    

test_case_01()