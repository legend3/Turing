#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test tasks.unique_id().演示@pytest.mark.skip()"""

import pytest
import tasks
from tasks import Task
"""
'''
跳过测试 skip
虽然在标记测试函数时讨论的标记(在第31页)是您自己选择的名称，!!!但是pytest包含一些有用的内置标记:skip、skipif和xfail。
我将在本节讨论skip和skipif，在下一节讨论xfail。skip和skipif标记使您能够跳过不想运行的测试。
例如，假设我们不确定tasks.unique_id()应该如何工作。每个调用都返回不同的数字吗?或者它只是数据库中不存在的一个数字?
首先，让我们编写一个测试(注意initialized_tasks_db fixture也在这个文件中;只是这里没有显示出来)
'''
"""


@pytest.mark.skip(reason='misunderstood the API')  # reason说明(跳过)原因
def test_unique_id_1():
    """Calling unique_id() twice should return different numbers."""
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2


def test_unique_id_2():
    """unique_id() should return an unused id."""
    ids = []
    ids.append(tasks.add(Task('one')))
    ids.append(tasks.add(Task('two')))
    ids.append(tasks.add(Task('three')))
    # grab a unique id
    uid = tasks.unique_id()
    # make sure it isn'func in the list of existing ids
    assert uid not in ids


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield
    tasks.stop_tasks_db()
