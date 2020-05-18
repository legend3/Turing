#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2020-05-15 03:52:38
@lastTime: 2020-05-17 14:31:46
@FilePath: \Turing\20-MySQL\conftest.py
@Description: 
@version: 
'''


"""Define some fixtures to use in the project."""

import pytest
import tasks
from tasks import Task
import pymysql

'''
现在，让我们看看如何在Tasks项目中使用参数化fixture。到目前为止，所有测试都使用TinyDB。
但是我们希望保留我们的选项，直到项目的后期。因此，我们编写的任何代码，以及编写的任何测试，
都应该都使用到TinyDB和MongoDB
'''


@pytest.fixture(scope='session', params=('tiny', 'mongo'))
def tasks_db_session(tmpdir_factory, request):
    """Connect to db before tests, disconnect after."""
    temp_dir = tmpdir_factory.mktemp('temp')
    tasks.start_tasks_db(str(temp_dir), request.param)
    yield  # this is where the testing happens
    tasks.stop_tasks_db()


@pytest.fixture()
def tasks_db(tasks_db_session):
    """An empty tasks db."""
    tasks.delete_all()


# Reminder of Task constructor interface
# Task(summary=None, owner=None, done=False, id=None)
# Don'func set id, it's set by database
# owner and done are optional


@pytest.fixture(scope='session')
def tasks_just_a_few():
    """All summaries and owners are unique."""
    return (
        Task('Write some code', 'Brian', True),
        Task("Code review Brian's code", 'Katie', False),
        Task('Fix what Brian did', 'Michelle', False))


@pytest.fixture(scope='session')
def tasks_mult_per_owner():
    """Several owners with several tasks each."""
    return (
        Task('Make a cookie', 'Raphael'),
        Task('Use an emoji', 'Raphael'),
        Task('Move to Berlin', 'Raphael'),

        Task('Create', 'Michelle'),
        Task('Inspire', 'Michelle'),
        Task('Encourage', 'Michelle'),

        Task('Do a handstand', 'Daniel'),
        Task('Write some books', 'Daniel'),
        Task('Eat ice cream', 'Daniel'))


@pytest.fixture()
def db_with_3_tasks(tasks_db, tasks_just_a_few):
    """Connected db with 3 tasks, all unique."""
    for t in tasks_just_a_few:
        tasks.add(t)


@pytest.fixture()
def db_with_multi_per_owner(tasks_db, tasks_mult_per_owner):
    """Connected db with 9 tasks, 3 owners, all with 3 tasks."""
    for t in tasks_mult_per_owner:
        tasks.add(t)


@pytest.fixture()
def con():
    try:
        conn = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='cloud_note', 
                                charset='utf8mb4')
        print("\n连接数据路成功！")        
        yield conn
    except Exception as e:
        print("数据库连接异常", e)
    finally:
        conn.close()
        print("断开数据库！")