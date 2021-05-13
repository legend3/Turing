#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2021-04-26 00:53:17
lastTime: 2021-04-27 01:43:01
LastAuthor: Do not edit
FilePath: /Turing/difflibDemo/test3.py
Description: 
version: 
'''

import pytest
import difflib
from deepdiff import DeepDiff

l1 = None
l2 = None
with open('C:\\Users\\Administrator\\Desktop\\C.sql', 'r') as f1:
    l1 = f1.readlines()
    
with open('C:\\Users\\Administrator\\Desktop\\D.sql', 'r') as f2:
    l2 = f2.readlines()

# d = difflib.Differ()
# diff = d.compare(l1, l2)
# print(diff)
# print("\n".join(list(diff)))
def test():
    assert DeepDiff(l1, l2).items().__len__() == 0


