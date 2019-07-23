"""Test for expected exceptions from using the API wrong."""

import pytest
import tasks

'''
冒烟测试（局部）
    a. 预期异常
    b.测试函数的标记
    
1.
期待得到相应异常的断言：with pytest.raises(TypeError);如果没有引发异常，则测试失败。如果测试引发另一个异常（期待的异常），也则会失败。
2.
excinfo收集异常信息
excinfo.value.args[0]——>第一个异常值
3.
打标记
@pytest.mark.命名
执行参数:-m
执行组合：and or and not
'''

'''
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
def test_get_raises():#此方法是满足——>-m 'smoke and get'
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


def test_start_tasks_db_raises():
    """Make sure unsupported db raises an exception."""
    '''
        1.您放在as后面的变量名(本例中为excinfo)充满了关于异常的信息，类型为ExceptionInfo
        2.提取异常的第一个值，希望确保异常的第一个(也是惟一的)参数匹配字符串（期待的异常报错信息）
        3.断言是否是期待的异常信息
    '''
    with pytest.raises(ValueError) as excinfo:
        tasks.start_tasks_db('some/great/path', 'mysql')
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "db_type must be a 'tiny' or 'mongo'"
