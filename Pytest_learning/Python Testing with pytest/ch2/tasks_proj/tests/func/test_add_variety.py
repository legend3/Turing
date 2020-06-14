"""Test the tasks.add() API function."""

import pytest
import tasks
from tasks import Task

"""
——参数化Pytest测试
通过函数发送一些值并检查输出以确保它是正确的，这是软件测试中常见的模式。
然而，仅使用一组值和一次检查正确性来调用一个函数，还不足以完全测试大多数函数。
参数化测试是一种通过相同的测试发送多个数据集的方法，如果其中任何一个测试集失败，就会有pytest报告。
为了帮助理解参数化测试试图解决的问题，让我们对add()做一个简单的测试:
"""

'''
用例说明：
创建任务对象时，将其id字段设置为None。在从数据库中添加和检索任务之后，id字段将被设置。
因此，我们不能仅仅使用==来检查是否正确地添加和检索了任务。等效()helper函数检查除id字段之外的所有字段。
包含autouse fixture，以确保数据库是可访问的。让我们确保考试通过
'''


def test_add_1():
    """tasks.get() using id returned from add() works."""
    task = Task('breathe', 'BRIAN', True)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    # everything but the id should be the same
    assert equivalent(t_from_db, task)


def equivalent(t1, t2):
    """Check two tasks for equivalence."""
    # Compare everything but the id field
    return ((t1.summary == t2.summary) and
            (t1.owner == t2.owner) and
            (t1.done == t2.done))

# 自动调用，保证对接上数据库
@pytest.fixture(autouse=True)  # （所有函数都会自动调用此fixture）
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield
    tasks.stop_tasks_db()


'''
2.
参数化pytest测试：  
                    @pytest.mark.parametrize('参数化命名',[])

如果我们想要测试一项任务的许多变化呢?没有问题。我们可以使用
@pytest.mark.parametrize(argnames, argvalues)，通过相同的测试传递大量数据

@pytest.mark.parametrize()的第一个参数是一个字符串，其中包含一个逗号分隔的名称列表“task”，在我们的示例中。
第二个参数是值列表，在我们的示例中是任务对象列表。pytest将为每个任务运行此测试一次，并将每个任务作为单独的测试报告

test_add_variety.py::test_add_2[task0] PASSED                            [ 25%]
test_add_variety.py::test_add_2[task1] PASSED                            [ 50%]
test_add_variety.py::test_add_2[task2] PASSED                            [ 75%]
test_add_variety.py::test_add_2[task3] PASSED                            [100%]
-标识符:    [task0]
'''


@pytest.mark.parametrize('task',
                         [
                          Task('sleep', done=True),
                          Task('wake', 'brian'),
                          Task('breathe', 'BRIAN', True),
                          Task('exercise', 'BrIaN', False)
                          ])
def test_add_2(task):
    """Demonstrate parametrize with one parameter."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


"""
3.
让我们将任务作为元组传递进来，看看多个测试参数是如何工作的:

3.1
当您使用pytest的易于转换为字符串的类型时，测试标识符使用报告中的参数值使其可读
test_add_variety.py::test_add_3[sleep-None-False] PASSED                 [ 25%]
test_add_variety.py::test_add_3[wake-brian-False] PASSED                 [ 50%]
test_add_variety.py::test_add_3[breathe-BRIAN-True] PASSED               [ 75%]
test_add_variety.py::test_add_3[eat eggs-BrIaN-False] PASSED             [100%]
*3.2
如果需要，可以使用整个测试标识符(在pytest术语中称为节点)重新运行测试:
pytest -v test_add_variety.py::test_add_3[sleep-None-False]

===================== test session starts ======================
collected 1 item
test_add_variety.py::test_add_3[sleep-None-False] PASSED
=================== 1 passed in 0.02 seconds ===================
"""


@pytest.mark.parametrize('summary, owner, done',  # 将任务作为元组传递进来
                         [('sleep', None, False),
                          ('wake', 'brian', False),
                          ('breathe', 'BRIAN', True),
                          ('eat eggs', 'BrIaN', False),
                          ])
def test_add_3(summary, owner, done):
    """Demonstrate parametrize with multiple parameters."""
    task = Task(summary, owner, done)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)
# ！可以只执行一组元素：pytest -q "test_add_variety.py::test_add_3['sleep', None, False]"

"""
3.3
如果标识符中有空格，请确保使用引号
pytest -v "test_add_variety.py::test_add_3[eat eggs-BrIaN-False]"
"""

"""
3.4
# 被参数化的必须为一个集合list;命名必须使用""包括，集合中每组元素可以为一个元组，元组中各元素可以在命名中用逗号隔开！
"""
# test_data2 = ("hello") # 会把字符串拆分为字母当成一个一个参数
test_data2 = ["hello"]
# test_data2 = (["hello"])  # 或者元组中包裹成列表


@pytest.mark.parametrize("s", test_data2)
def test_b(s):
    assert s == "hello"


"""
将任务列表移动到函数外部的一个变量:（可读性不好，输出不显示tasks_to_try元组中数据数据列表值）
"""
tasks_to_try = (Task('sleep', done=True),
                Task('wake', 'brian'),
                Task('wake', 'brian'),
                Task('breathe', 'BRIAN', True),
                Task('exercise', 'BrIaN', False))


@pytest.mark.parametrize('task', tasks_to_try)
def test_add_4(task):
    """Slightly different take."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


'''
4.
——可以通过ids关键字来自定义一个字符串（或字符串列表中的字符串）来表示测试ID

the multiple parameter version的可读性很好，但是Task对象列表也是如此(4的问题)。
为了解决这个问题，我们可以使用ids optional参数来参数化()来为每个task数据创建自己定义的标识符。
但是，由于我们将数据分配由变量名tasks_to_try，因此可以使用它来生成id
'''


# 列表推导式后，ids能对列表中各元素(一个Task实例数据列表)作标记
task_ids = ['Task({},{},{})'.format(t.summary, t.owner, t.done) for t in tasks_to_try]  # 创建一个集合，集合元素为为@pytest.mark.parametrize定义ids


@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)  # ids给taks的每个任务数据定义标识符；taks_to_try给taks传值
def test_add_5(task):
    """Demonstrate ids."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    # print("打印：",type(task_ids),task_ids)
    assert equivalent(t_from_db, task)


'''
这些自定义的测试标识符可以用来运行测试
$ cd /path/to/code/ch2/tasks_proj/tests/func
$ pytest -v "test_add_variety.py::test_add_5[Task(exercise,BrIaN,False)]"# 我们确实需要这些标识符的引号;否则，括号和圆括号将混淆shell

输出：
===================== test session starts ======================
collected 1 item
test_add_variety.py::test_add_5[Task(exercise,BrIaN,False)] PASSED
=================== 1 passed in 0.03 seconds ===================
'''

'''
还可以通过在@pytest.mark.parametrize()装饰器中传入列表时在参数值旁边加上id来标识参数。
可以这样来做。参pytest.param(<Value>,id='something')

@pytest.mark.parametrize 添加ID标识
语法为： pytest.param(<Value>,id='something')
'''


# task元素自带id
@pytest.mark.parametrize('task', [  # 1.直接
    pytest.param(Task('create'), id='just summary'),
    pytest.param(Task('inspire', 'Michelle'), id='summary/owner'),
    pytest.param(Task('encourage', 'Michelle', True), id='summary/owner/done')])

def test_add_6(task):
    """Demonstrate pytest.param and id."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


tasks_to_try2 = (pytest.param(Task('sleep', done=True),id='id1'),  # 2.将任务列表移动到函数外部的一个变量
                 pytest.param(Task('wake', 'brian'),id='id2'),
                 pytest.param(Task('wake', 'brian'),id='id3'),
                 pytest.param(Task('breathe', 'BRIAN', True),id='id4'),
                 pytest.param(Task('exercise', 'BrIaN', False),id='id5'))


@pytest.mark.parametrize('task',tasks_to_try2)
def test_add_7(task):
    """Demonstrate pytest.param and id."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


"""
还可以将parametertrize()应用于类。当您这样做时，相同的数据将被发送到类中的所有测试方法
"""
@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
class TestAdd():  # 参数化的类必须每个方法都带'task'作为参数
    """Demonstrate parametrize and test classes."""

    def test_equivalent(self, task):
        """Similar test, just within a class."""
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert equivalent(t_from_db, task)

    def test_valid_id(self, task):
        """We can use the same data for multiple tests."""
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert t_from_db.id == task_id


if __name__ == '__main__':
    tasks_to_try = (Task('sleep', done=True),
                Task('wake', 'brian'),
                Task('wake', 'brian'),
                Task('breathe', 'BRIAN', True),
                Task('exercise', 'BrIaN', False))
    task_ids = ['Task({},{},{})'.format(t.summary, t.owner, t.done) for t in tasks_to_try] 
    print(task_ids)

    l = [1,2,3]
    id = [4 if t is 2 else t for t in l]  # 替换列表中的
    print(id)