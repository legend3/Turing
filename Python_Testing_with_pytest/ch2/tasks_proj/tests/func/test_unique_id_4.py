"""Test tasks.unique_id().演示@pytest.mark.xfail(条件,reason="")"""

import pytest
import tasks
from tasks import Task
"""
xfail
标记预期会失败的测试 xfail
使用skip和skipif标记，即使跳过测试也不会尝试。
使用xfail标记，我们告诉pytest运行一个测试函数，但是我们预期它会失败。
让我们再次修改unique_id()测试，以使用xfail

1.
.代表PASSED
F代表FAILED
x代表XFAIL，“预计断言会失败，确实出错了”,但report不报错：pytest.ini文件配置xfail_strict=true
X代表XPASS，“预计断言会失败但没失败” 

2.
*或者，您也可以在测试或设置函数中强制地将一个测试标记为XFAIL:
def test_function():
    if not valid_config():
        pytest.xfail("failing configuration (but should work)")
这将无条件地使est_function XFAIL。*注意，pytest.xfail调用之后不执行其他代码。与标记不同。这是因为它是通过在内部引发一个已知异常来实现的。
"""
@pytest.mark.xfail(tasks.__version__ < '0.2.0',reason='not supported until version 0.2.0')
def test_unique_id_1():
    """Calling unique_id() twice should return different numbers."""
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2  # 实际是相等


'''
True，被标记的测试函数(预计是错)，确实出错了为XFAIL;未出错就为XPASS。
2.
    pytest.ini中配置
    xfail_strict=true,未出错则为FAILED
False，@pytest.mark.xfail不生效
'''
@pytest.mark.xfail(condition=True,reason="uid should is int")
def test_unique_id_is_a_duck():
    """Demonstrate xfail."""
    uid = tasks.unique_id()
    assert uid == 'a duck'


@pytest.mark.xfail()
def test_unique_id_not_a_duck():
    """Demonstrate xpass."""
    uid = tasks.unique_id()
    assert uid == 'a duck'


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