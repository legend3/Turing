"""Test for expected exceptions from using the API wrong."""

import pytest
import tasks
import pymysql

'''
冒烟测试（局部）
    a.预期异常
    b.测试函数的标记
    
1.
期待得到相应异常的断言：with pytest.raises(TypeError);如果没有引发异常，则测试失败。
如果测试引发另一个异常（期待的异常），也则会失败。
excinfo收集异常信息
excinfo.value.args[0]——>第一个异常值
2.
打标记
@pytest.mark.命名
执行参数:-m
执行组合：and or and not
'''

'''
——项目说明
api.py:
def add(task): # type: (Task) -> int            type:参数类型   返回值init
def get(task_id): # type: (int) -> Task
def list_tasks(owner=None): # type: (str|None) -> list of Task
def count(): # type: (None) -> int
def update(task_id, task): # type: (int, Task) -> None
def delete(task_id): # type: (int) -> None
def delete_all(): # type: () -> None
def unique_id(): # type: () -> int
def start_tasks_db(db_path, db_type): # type: (str, str) -> None
def stop_tasks_db(): # type: () -> None
'''

'''
——场景说明
在clic .py中的CLI代码和API .py中的API代码之间，对于将向API函数发送什么类型，有一个协议。
如果类型错误，我希望在这些API调用中引发异常。
为了确保这些函数在调用不正确时引发异常，让我们在测试函数中使用错误的类型来故意导致类型错误异常，
并与pytest.raise()一起使用，就像这样


——with pytest.raise (TypeError)函数解析
语句表示，下一个代码块中的任何内容都应该引发一个TypeError异常。
如果没有引发异常，则测试失败。如果测试引发另一个异常，则意味代码执行失败
'''


def test_add_raises():
    """add() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.add(task='not a Task object')


@pytest.mark.smoke
def test_list_raises():
    """list() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.list_tasks(owner=123)


@pytest.mark.get
@pytest.mark.smoke
def test_get_raises():  # 此方法是满足——>-m 'smoke and get'
    """get() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.get(task_id='123')


class TestUpdate():
    """Test expected exceptions with tasks.update()."""

    def test_bad_id(self):
        """A non-int id should raise an excption."""
        with pytest.raises(TypeError):
            tasks.update(task_id={'dict instead': 1},
                         task=tasks.Task())

    def test_bad_task(self):
        """A non-Task task should raise an excption."""
        with pytest.raises(TypeError):
            tasks.update(task_id=1, task='not a task')


def test_delete_raises():
    """delete() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.delete(task_id=(1, 2, 3))


'''
我们刚刚检查了test_add_raise()中的异常类型。你也可以查看
异常的参数。对于start_tasks_db(db_path, db_type)， db_type不仅需要是字符串，还必须是“tiny”或“mongo”。你可以
检查，以确保异常消息是正确的添加为excinfo:
'''


def test_start_tasks_db_raises():
    """Make sure unsupported db raises an exception."""
    """自定义异常的异常内容，利用pytest的raises方法(只是)捕获事先start_tasks_db方法中自定义的异常内容"""
    '''
        1.您放在as后面的变量名(本例中为excinfo)充满了关于异常的信息，类型为ExceptionInfo
        2.提取异常的第一个值，希望确保异常的第一个(也是惟一的)参数匹配字符串（期待的异常报错信息）
        3.断言是否是期待的异常信息
    '''
    with pytest.raises(ValueError) as excinfo:  # 被测函数自定义的异常是否能正常被抛出
        tasks.start_tasks_db('some/great/path', 'mysql')
    exception_msg = excinfo.value.args[0]
    print(exception_msg)
    assert exception_msg == "db_type must be a 'tiny' or 'mongo'"
    