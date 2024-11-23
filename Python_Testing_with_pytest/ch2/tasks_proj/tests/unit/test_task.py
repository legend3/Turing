#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2019-12-22 11:35:22
lastTime: 2024-06-16 19:22:53
LastAuthor: Do not edit
FilePath: /Python_Testing_with_pytest/ch2/tasks_proj/tests/unit/test_task.py
Description: 
version: 
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test the Task data type."""
from tasks import Task

'''
与test_three、test_four不同是：已经导入了Task项目
断言：assert；（正确）
'''


def test_asdict():
    """_asdict() should return a dictionary."""
    t_task = Task('do something', 'okken', True, 21)
    t_dict = t_task._asdict()  # 返回一个元素名与元素值键值对的字典<class 'collections.OrderedDict'>
    expected = {'summary': 'do something',
                'owner': 'okken',
                'done': True,
                'id': 21}
    assert t_dict == expected


def test_replace():
    """replace() should change passed in fields."""
    t_before = Task('finish book', 'brian', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'brian', True, 10)
    assert t_after == t_expected


def test_defaults():
    """Using no parameters should invoke defaults."""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2


def test_member_access():
    """Check .field functionality of namedtuple."""
    t = Task('buy milk', 'brian')
    assert t.summary == 'buy milk'
    assert t.owner == 'brian'
    assert (t.done, t.id) == (False, None)
