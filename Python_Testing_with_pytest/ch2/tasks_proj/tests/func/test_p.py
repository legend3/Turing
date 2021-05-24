#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2020-06-14 18:22:28
lastTime: 2021-05-20 02:02:26
LastAuthor: Do not edit
FilePath: /Turing/Python_Testing_with_pytest/ch2/tasks_proj/tests/func/test_p.py
Description: 
version: 
'''

import pytest
from tinydb import Query

# l = None
l2 = ("d", "e", "f")

l3 = None

lid = [1, 2, 3]
# ids = [i for i in lid]


class Test():
    def test_02(self, initTinyDB):
        # global l
        l = ['a','b','c']
        initTinyDB.insert({'li': l})
        # for item in initTinyDB:
        #     print(item)
        # print(initTinyDB.all()[0]['li'])
        # print(initTinyDB.search(Query()))

    @pytest.fixture(params=initTinyDB.all()[0]['li'])
    def a(self, request):
        return request.param


    @pytest.mark.parametrize('l2', l2, ids=lid)
    def test_b(self, l2, a):
        print("a：", a)

