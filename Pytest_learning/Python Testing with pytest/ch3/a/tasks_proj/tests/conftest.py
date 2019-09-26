"""Define some fixtures to use in the project."""

import pytest
import tasks
from tasks import Task

"""
Fixture

——前沿
既然您已经了解了pytest的基础知识，那么让我们将注意力转向fixture，它对于构建几乎任何非平凡软件系统的测试代码都是必不可少的。

fixture是pytest在实际测试函数之前(有时是之后)运行的函数。*fixture中的代码可以做您想做的任何事情。
您可以使用fixture为要处理的测试获取数据集。在运行测试之前，可以使用fixture使系统进入已知状态。fixture还用于为多个测试准备数据.

—我们可以简单的把Fixture理解为准备测试数据和初始化测试对象的阶段。
    一般我们对测试数据和测试对象的管理有这样的一些场景:
    所有用例开始之前初始化测试数据或对象
    所有用例结束之后销毁测试数据或对象
    每个用例开始之前初始化测试数据或对象
    每个用例结束之后销毁测试数据或对象
    在每个／所有module的用例开始之前初始化数据或对象
    在每个／所有module的用例开始之后销毁数据或对象
    ......
    ......
pytest的fixture特性可以满足上面的需求。

1.
fixture()装饰器用于告诉pytest函数是一个fixture。当您在测试函数的参数列表中包含fixture名称时，pytest知道在运行测试之前要运行它。
fixture可以执行工作，也可以向测试函数返回数据。test test_some_data()具有fixture的名称some_data作为参数。pytest将看到这一点，并寻找具有此名称的fixture。
命名在pytest中非常重要。pytest将在测试模块中查找该名称的fixture。如果没有在这个文件中找到它，它还会在conftest.py文件中查找。
2.
在开始研究fixture(以及conftest.py文件)之前，我需要说明这样一个事实:fixture这个术语在编程和测试社区中有很多含义，甚至在Python社区中也是如此。
我可以互换使用fixture、fixture函数和fixture方法来引用本章讨论的@pytest.fixture()修饰函数。Fixture还可以用来引用Fixture函数正在设置的资源。
Fixture函数通常设置或检索一些测试可以使用的数据。有时，这些数据被认为是固定的。
例如，Django社区经常使用fixture表示在应用程序开始时加载到数据库中的一些初始数据。无
论其他含义如何，在pytest和本书中，测试fixture都是指pytest提供的机制，该机制允许从测试函数中分离出准备代码和清理代码之后的代码。
pytest fixture是使pytest在其他测试框架中脱颖而出的独特核心特性之一，也是许多人转而使用并继续使用pytest的原因。
但是，pytest中的fixture不同于Django中的fixture，也不同于unittest和nose中的安装和拆卸过程。关于fixture有很多特性和细微差别。
一旦你对它们的工作原理有了一个很好的心理模型，它们对你来说就会变得很容易。然而，你必须和他们玩一段时间，所以让我们开始吧。
3.
您可以将fixture放入单独的测试文件中，但是要在多个测试文件之间共享fixture，您需要使用位于所有测试中心位置的conftest.py文件。
对于Tasks项目，所有fixture都位于tasks_proj/tests/conftest.py中。从那里，fixture可以被任何测试共享。
如果您希望fixture只被该文件中的测试使用，那么可以将fixture放在单独的测试文件中。
同样，您也可以在顶部测试目录的子目录中包含其他conftest.py文件。
如果您这样做了，那么在这些低层conftest.py文件中定义的fixture将对该目录和子目录中的测试可用。
然而，到目前为止，Tasks项目中的fixture是用于任何测试的。因此，将所有fixture放在测试根目录tasks_proj/tests的conftest.py文件中最有意义。
尽管conftest.py是一个Python模块，但是它不应该被测试文件导入。不要从任何地方import conftest。
conftest.py文件被pytest读取，并被认为是一个本地插件，这在我们开始讨论第3章时就很有意义了。
py文件被pytest读取，并被认为是一个本地插件，一旦我们开始在第5章(第95页的plugins)中讨论插件，这就很有意义了。
现在，将tests/conftest.py看作是一个地方，我们可以将所有测试使用的fixture放在tests目录下。
"""


'''
1.
tmpdir的值不是字符串，而是表示目录的对象。
但是，它实现了_str__，所以我们可以使用str()来获得一个字符串来传递给start_tasks_db()。目前，我们仍然在TinyDB中使用tiny
2.
fixture函数在的测试之前运行使用它。但是，如果函数中有一个yield，它就会停止，将控制传递给测试，并在测试完成后继续下一行。
因此，将yield上面的代码看作是setup, yield之后的代码看作是teardown。
不管测试期间发生了什么，在yield(拆下)之后的代码都保证运行。我们不返回任何数据与产量在这个fixture。但是你可以。
'''

'''
返回一个临时目录路径对象，它是每个测试函数调用的惟一对象，创建为基本临时目录的子目录。返回的对象是“py.path”。当地的_路径对象
'''
@pytest.fixture()
def tasks_db(tmpdir):
    """Connect to db before tests, disconnect after."""
    # Setup : start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield  # this is where the testing happens

    # Teardown : stop db
    tasks.stop_tasks_db()


'''
这些fixture都在各自的参数列表中包含两个fixture: tasks_db和一个数据集(tasks_just_a_few、tasks_mult_per_owner)。数据集用于向数据库添加任务。
现在，当您希望测试从非空数据库开始时，可以使用这些参数
'''
# Reminder of Task constructor interface
# Task(summary=None, owner=None, done=False, id=None)
# summary is required
# owner and done are optional
# id is set by database


@pytest.fixture()
def tasks_just_a_few():
    """All summaries and owners are unique."""
    return (
        Task('Write some code', 'Brian', True),
        Task("Code review Brian's code", 'Katie', False),
        Task('Fix what Brian did', 'Michelle', False))


@pytest.fixture()
def tasks_mult_per_owner():
    """Several owners with several tasks each."""
    return (
        Task('Make a cookie', 'Raphael'),
        Task('Use an emoji', 'Raphael'),
        Task('Move to Berlin', 'Raphael'),

        Task('Create', 'Michelle'),
        Task('Inspire', 'Michelle'),
        Task('Encourage', 'Michelle'),

        Task('Do a handstand', 'Daniel'),
        Task('Write some books', 'Daniel'),
        Task('Eat ice cream', 'Daniel'))


'''
Using Multiple Fixtures多重Fixtures
'''
# 1
@pytest.fixture()
def db_with_3_tasks(tasks_db, tasks_just_a_few):
    """Connected db with 3 tasks, all unique."""
    for t in tasks_just_a_few:
        tasks.add(t)


@pytest.fixture()
def db_with_multi_per_owner(tasks_db, tasks_mult_per_owner):
    """Connected db with 9 tasks, 3 owners, all with 3 tasks."""
    for t in tasks_mult_per_owner:
        tasks.add(t)
