"""Test the tasks.add() API function."""

import pytest
import tasks
from tasks import Task

'''
@pytest.fixture

“With parametrized functions, you get to run that function multiple times. But
with parametrized fixtures, every test function that uses that fixture will be
called multiple times. Very powerful”
1.可以定义到conftest.py起到全局使用的作用；函数参数化只能对当前函数上使用
'''

tasks_to_try = (Task('sleep', done=True),
                Task('wake', 'brian'),
                Task('breathe', 'BRIAN', True),
                Task('exercise', 'BrIaN', False))

task_ids = ['Task({},{},{})'.format(t.summary, t.owner, t.done) for t in tasks_to_try[0:1]]

def equivalent(t1, t2):
    """Check two tasks for equivalence."""
    return ((t1.summary == t2.summary) and
            (t1.owner == t2.owner) and
            (t1.done == t2.done))
#
#params它将导致多个参数调用fixture函数和所有测试使用它
@pytest.fixture(params=tasks_to_try)
def a_task(request):#request等同'task',传入值
    """Using no ids."""
    return request.param


def test_add_a(tasks_db, a_task):#利用a_task的返回值
    """Using a_task fixture (no ids)."""
    task_id = tasks.add(a_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, a_task)
#
#
@pytest.fixture(params=tasks_to_try[0:1], ids=task_ids)#params的值要与ids的值一一对应
def b_task(request):
    """Using a list of ids."""
    return request.param


def test_add_b(tasks_db, b_task):
    """Using b_task fixture, with ids."""
    task_id = tasks.add(b_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, b_task)


#函数化推导式
def id_func(fixture_value):
    """A function for generating ids."""
    t = fixture_value
    return 'Task({},{},{})'.format(t.summary, t.owner, t.done)#返回一个Task实例的地址下表

#只取tasks_to_try元组中部分Task()元素,id_func()函数形式。（tasks_to_try与id_func数量要保持一致）
@pytest.fixture(params=tasks_to_try[0:1], ids=id_func)
def c_task(request):
    """Using a function (id_func) to generate ids."""
    return request.param

def test_add_c(tasks_db, c_task):
    """Use fixture with generated ids."""
    task_id = tasks.add(c_task)
    t_from_db = tasks.get(task_id)
    print(id_func(Task))
    assert equivalent(t_from_db, c_task)