"""Test the tasks.add() API function."""

import pytest
import tasks
from tasks import Task

'''
完整的冒烟测试
    a.测试函数的标记
    b.初始fixture
'''


def test_add_returns_valid_id():
    """tasks.add(<valid task>) should return an integer."""
    # GIVEN an initialized tasks db
    # WHEN a new task is added
    # THEN returned task_id is of type int
    new_task = Task('do something')
    task_id = tasks.add(new_task)
    """
        isinstance() 与 type() 区别：
        type() 不会认为子类是一种父类类型，不考虑继承关系。
        isinstance() 会认为子类是一种父类类型，考虑继承关系。
        如果要判断两个类型是否相同推荐使用 isinstance()。
    """
    assert isinstance(task_id, int)


@pytest.mark.smoke
def test_added_task_has_id_set():
    """Make sure the task_id field is set by tasks.add()."""
    # GIVEN an initialized tasks db
    #   AND a new task is added
    new_task = Task('sit in chair', owner='me', done=True)
    task_id = tasks.add(new_task)

    # WHEN task is retrieved
    task_from_db = tasks.get(task_id)

    # THEN task_id matches id field
    assert task_from_db.id == task_id


"""
1.
场景使用：当测试集中有需要提前初始或调用的测试用例，或需要后续做些处理方面的，方使用此场景

2.
这两个(上述)测试都具有给定初始化任务db的注释，但是测试中没有初始化数据库。我们可以定义一个fixture来在测试前初始化数据库，
并在测试后清理数据库

在我们的测试中使用的autouse表明该文件中的所有测试都将调用initialized_tasks_db(tmpdir)。
yield运行前的代码在每次测试前运行;yield之后的代码在测试之后运行。
如果需要，yield可以将数据返回给测试。
"""
@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    # Setup : start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield  # this is where the testing happens

    # Teardown : stop db
    tasks.stop_tasks_db()
