"""Define some fixtures to use in the project."""

import pytest
import tasks
from tasks import Task


@pytest.fixture(scope='session')
def tasks_db_session(tmpdir_factory, request):
    """Connect to db before tests, disconnect after."""
    temp_dir = tmpdir_factory.mktemp('temp')
    tasks.start_tasks_db(str(temp_dir), 'tiny')
    yield  # this is where the testing happens
    tasks.stop_tasks_db()


@pytest.fixture()
def tasks_db(tasks_db_session):
    """An empty tasks db."""
    tasks.delete_all()


# Reminder of Task constructor interface
# Task(summary=None, owner=None, done=False, id=None)
# Don'func set id, it's set by database
# owner and done are optional


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


'''
1.
插件的作用：第三方插件包含相当多的代码。这就是我们使用它们来节省我们自己开发所有代码的时间的原因之一。
然而，对于您特定的编码域，您无疑会提出特殊的fixture和修改来帮助您进行测试。
通过创建插件，您可以轻松地在几个项目之间共享少量的fixture
插件定义描述：插件可以包含改变pytest行为的hook函数。
因为pytest的目的是允许插件改变pytest的行为方式，所以有很多hook函数可用。
pytest的hook函数被指定在pytest文档站点上

插件的创建布局模式(不一定，但很调理)：为了将行为变化与插件机制的讨论分开！！！
1.（hook在conftest.py中）在将其转换为可分发的插件之前我们将我们的修改放在conftest.py中；那样修改(插件)不仅仅在一个项目中被使用而且将变得可以共享、扩展
'''


# 可以扩展向标头添加信息的功能，以添加用户名并指定使用的硬件和测试版本。
# 实际上，任何可以转换成字符串的东西，都可以填入测试头。
def pytest_report_header():  # 一个hook函数
    """Thank tester for running tests."""
    return "Thanks for running the tests."


'''
report-->class:TestReport，继承了BasicReport类;
基本测试报告对象(也用于setup和teardown的调用执行，如果它们失败)。
nodeid,规范化收集节点id
location,一个(filesystempath, lineno, domaininfo)元组表示一个测试项的实际位置——它可能与收集到的不同，
例如，如果一个方法是从另一个模块继承来的。
keywords,名称->值字典，包含与测试调用相关联的所有关键字和标记。
outcome,测试结果，总是“passed”, “failed”, “skipped”其中之一（如果要修改outcome，则用report.状态判断，然后返回）
longrepr,None或者一个fail的表示
when, 表示测试阶段的‘setup’, ‘call’, ‘teardown’的其中之一
user_properties，一个包含用户定义的测试属性的元组列表(名称、值)
sections=(),
duration=0,获取仅执行测试的时间
from_item_and_call(item, call)[source],工厂方法来，用item和call的信息创建填充一个TestReport
caplog,如果日志捕获启用，则返回捕获的日志行
capstderr，如果(stderr)已启用捕获，则从stderr返回捕获的文本
capstdout，如果(stdout)已启用捕获，则从stdout返回捕获的文本
count_towards_summary
    Experimental
head_line
    Experimenta
longreprtext,
'''


def pytest_report_teststatus(report):  # 一个hook函数
    """Turn failures into opportunities."""
    # print(report.nodeid,
    #       report.location,
    #       report.keywords,
    #       report.user_properties,
    #       report.duration,
    #       report.caplog,
    #       report.capstderr,
    #       report.outcome,
    #       report.when,
    #       sep="\n")
    if report.when == 'call' and report.failed:  # 测试call阶段时 and 测试失败时
            return (report.outcome, 'O', 'OPPORTUNITY for improvement')  # 报告状态为F时改为O，为FAILDED时改为'OPPORTUNITY for improvement'

    if report.when == 'call' and report.passed:  # 测试call阶段时 and 测试成功时
            return (report.outcome, 'OK', 'Everythin is OK!')  # 报告状态为.时改为OK，为PASSED时改为'Everythin is OK!'


# 自定义mark
def pytest_configure(config):
    markers_list = ["smoke","get"]
    for markers in markers_list:
        config.addinivalue_line("markers", markers)
