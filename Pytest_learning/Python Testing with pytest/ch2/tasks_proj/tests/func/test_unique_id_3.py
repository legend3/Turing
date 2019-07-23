"""Test tasks.unique_id()."""

import pytest
import tasks
from tasks import Task

'''
skipif
假设由于某种原因，我们决定第一个测试也应该是有效的，并且我们打算在包的0.2.0版本中实现这一点。我们可以不进行测试，而是使用skipif

"条件跳过"——>skipif(条件,reason='xxxxx')    not supported until version 0.2.0
    1.条件：我们传递给skipif()的表达式可以是任何有效的Python表达式。在本例中，我们正在检查包版本
    2.原因：reason，在skip中不是必需的，但在skipif中是必需的。我喜欢为每次跳过、跳过if或xfail添加一个原因
    显示参数：-r,由特殊的字符显示指定的额外测试摘要信息summary info：(f)尾随，(E)错误，(s)跳过，(x)失败，(x)通过，(p)通过，(p)通过输出，(a)除pP外全部通过
    执行：pytest -rs test_xxxx.py
'''
@pytest.mark.skipif(tasks.__version__ < '0.2.0',
                    reason='not supported until version 0.2.0')
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
    # make sure it isn't in the list of existing ids
    assert uid not in ids


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield
    tasks.stop_tasks_db()
