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


'''也可以通过安装pytest-nice插件增加自定义nice命令选项'''
def pytest_addoption(parser):  # 添加后只有命令行中有--nice选项，（下面）对报告状态的修改才能发生！
    """Turn nice features on with --nice option."""
    group = parser.getgroup('nice')  # 获取或创建一个命令选项命名的组
    group.addoption("--nice", action="store_true",  # 向该组添加一个命令选项
                    help="nice: turn failures into opportunities")


def pytest_report_header(config):  # hook函数(直接调用),返回一个字符串或字符串列表，显示为终端报告的标题信息。
    """Thank tester for running tests."""
    if config.getoption('nice'):
        return "Thanks for running the tests."


def pytest_report_teststatus(report, config):  # hook函(直接调用),返回结果类别、简短和冗长的报告词
    """Turn failures into opportunities."""
    if report.when == 'call':
        if report.failed and config.getoption('nice'):  # report.faile报告状态;config.getoption('nice')获取命令参数
            return (report.outcome, 'O', 'OPPORTUNITY for improvement')


'''也可以在pytest.ini文件中定义markers;此处在pytest.ini文件中配置,但要在pytest.ini文件所在的根目录下执行pytest及命令选项'''
# def pytest_configure(config):
#     markers_list = ["smoke","get"]
#     for marker in markers_list:
#         config.addinivalue_line("markers",marker)  # "markers"pytest内置的变量名称
