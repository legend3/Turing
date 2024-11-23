#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2019-12-22 11:35:22
lastTime: 2024-08-19 00:58:13
LastAuthor: Do not edit
FilePath: /Python_Testing_with_pytest/ch3/a/tasks_proj/tests/func/test_unique_id.py
Description: 
version: 
'''

"""Test tasks.unique_id()."""

import tasks


def test_unique_id(tasks_db, tasks_mult_per_owner):
    """unique_id() should return an unused id."""
    existing_tasks = tasks.list_tasks()
    uid = tasks.unique_id()
    for t in existing_tasks:
        assert uid != t.id
