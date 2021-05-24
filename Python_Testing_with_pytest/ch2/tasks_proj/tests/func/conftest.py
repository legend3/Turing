#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2021-05-20 00:44:48
lastTime: 2021-05-20 01:58:20
LastAuthor: Do not edit
FilePath: /Turing/Python_Testing_with_pytest/ch2/tasks_proj/tests/func/conftest.py
Description: 
version: 
'''
import pytest
from tinydb import TinyDB, Query

@pytest.fixture(scope='session')
def initTinyDB():
    db = TinyDB('mydb.json')
    yield db
    db.truncate()
    db.close()