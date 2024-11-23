#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test the tasks.add() API function."""

import pytest
import tasks
from tasks import Task

'''
1.
让我们更改一个task .add()测试来使用这个fixture    （conftest.py-->tasks_db(tmpdir)）
2.
当我开发fixture时,我喜欢查看运行的是什么,以及什么时候运行。幸运的是,pytest提供了一个命令行标志——setup-show,它就是这样做的。
$ pytest --setup-show test_add.py -k valid_id
===================== test session starts ======================
collected 3 items
test_add.py
SETUP S tmpdir_factory
SETUP F tmpdir (fixtures used: tmpdir_factory)
SETUP F tasks_db (fixtures used: tmpdir)
func/test_add.py::test_add_returns_valid_id
(fixtures used: tasks_db, tmpdir, tmpdir_factory).
TEARDOWN F tasks_db
TEARDOWN F tmpdir
TEARDOWN S tmpdir_factory
====================== 2 tests deselected ======================
============ 1 passed, 2 deselected in 0.02 seconds ============
3.
F和S表示范围:
F表示函数范围,
S表示会话范围。
'''


def test_add_returns_valid_id(tasks_db):
    """tasks.add(<valid task>) should return an integer."""
    # GIVEN an initialized tasks db
    # WHEN a new task is added
    # THEN returned task_id is of type int
    new_task = Task('do something')
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)


@pytest.mark.smoke
def test_added_task_has_id_set(tasks_db):
    """Make sure the task_id field is set by tasks.add()."""
    # GIVEN an initialized tasks db
    #   AND a new task is added
    new_task = Task('sit in chair', owner='me', done=True)
    task_id = tasks.add(new_task)

    # WHEN task is retrieved
    task_from_db = tasks.get(task_id)

    # THEN task_id matches id field
    assert task_from_db.id == task_id

    # AND contents are equivalent (except for id)
    # the [:-1] syntax returns a list with all but the last element
    assert task_from_db[:-1] == new_task[:-1]


'''
Using Multiple Fixtures多重Fixtures
多重fixture的意义: 
*fixture的一个重要原因:将测试集中在实际测试的内容上,而不是为准备测试而必须做的事情上。
我喜欢在给定/WHEN/THEN中使用注释,并尝试将给定的注释尽可能多地添加到fixture中,原因有两个。
首先,它使测试更具可读性,因此更易于维护。其次,fixture中的断言或异常会导致错误,而测试函数中的断言或异常会导致失败。
如果数据库初始化失败,我不希望test_add_increes_count()失败。
那只能是被拒绝。我希望test_add_increes_count()只有在add()确实无法更改计数时才可能失败
'''
# 2


def test_add_increases_count(db_with_3_tasks):  # db_with_3_tasks测试的准备
    """Test tasks.add() affect on tasks.count()."""
    # GIVEN a db with 3 tasks
    #  WHEN another task is added
    tasks.add(Task('throw a party'))  # 测试的重点


    #  THEN the count increases by 1
    assert tasks.count() == 4
