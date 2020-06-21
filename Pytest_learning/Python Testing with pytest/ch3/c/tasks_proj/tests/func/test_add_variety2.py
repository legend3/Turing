#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2019-12-22 11:35:22
@lastTime: 2020-06-16 01:46:27
@LastAuthor: Do not edit
@FilePath: \Turing\Pytest_learning\Python Testing with pytest\ch3\c\tasks_proj\tests\func\test_add_variety2.py
@Description: 
@version: 
'''


"""Test the tasks.add() API function."""

import pytest
import tasks
from tasks import Task
import os

tasks_to_try = (Task('sleep', done=True),
                Task('wake', 'brian'),
                Task('breathe', 'BRIAN', True),
                Task('exercise', 'BrIaN', False))

task_ids = ['Task({},{},{})'.format(t.summary, t.owner, t.done)
            for t in tasks_to_try]


def equivalent(t1, t2):
    """Check two tasks for equivalence."""
    return ((t1.summary == t2.summary) and
            (t1.owner == t2.owner) and
            (t1.done == t2.done))


@pytest.fixture(params=tasks_to_try)
def a_task(request):
    print("\n",request.param)
    return request.param


def test_add_a(tasks_db, a_task):
    task_id = tasks.add(a_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, a_task)


@pytest.fixture(params=tasks_to_try, ids=task_ids)
def b_task(request):
    return request.param


def test_add_b(tasks_db, b_task):
    task_id = tasks.add(b_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, b_task)


def id_func(fixture_value):
    """A function for generating ids."""
    t = fixture_value
    return 'Task({},{},{})'.format(t.summary, t.owner, t.done)


@pytest.fixture(params=tasks_to_try, ids=id_func)
def c_task(request):
    """Using a function (id_func) to generate ids."""
    return request.param


def test_add_c(tasks_db, c_task):
    """Use fixture with generated ids."""
    task_id = tasks.add(c_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, c_task)


# 补充：@pytest.mark.parametrize('yyy', yyy,ids=ids)调用fixtrue(params=xxxx, ids=ids)
l = ("a", "b", "c")
l2 = ("d", "e", "f")

lid = [1, 2, 3]
ids = [i for i in lid]


@pytest.fixture(params=l, ids=ids)
def test_a(request):
    return request.param


@pytest.mark.parametrize('l2', l2,ids=ids)
def test_b(l2, test_a):
    print("l2参数：", l2)

# 总结：每执行一个fixtrue(params=xxxx, ids=ids)后，执行一遍所有@pytest.mark.parametrize('yyy', yyy,ids=ids)

