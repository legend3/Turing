"""Define some fixtures to use in the project."""

import pytest
import tasks
from tasks import Task

'''
Changing Scope for Tasks Project Fixtures——更改项目Fixtures的任务范围

1.
要使tasks_db之类的东西成为会话范围，您需要使用tmpdir_factory，因为tmpdir是function范围，而tmpdir_factory是seesion范围。
幸运的是，这只是一个单行代码更改(如果在参数列表中计算tmpdir -> tmpdir_factory，则为2)
2.
这里，我们将tasks_db更改为依赖于tasks_db_session，并删除了所有条目以确保它是空的。
因为我们没有更改它的名称，所以已经包含它(tasks_db)的fixture或测试都没有被更改。
3.
数据fixture只返回一个值，所以没有理由让它们一直运行。
每个sesion一次就足够了

'''
# 确保并避免了tasks_db()处于与数据库保持连接且为数据库设置临时目录（需要时就清空数据库）
@pytest.fixture(scope='session')
def tasks_db_session(tmpdir_factory):
    """Connect to db before tests, disconnect after."""
    temp_dir = tmpdir_factory.mktemp('temp')
    tasks.start_tasks_db(str(temp_dir), 'tiny')
    yield
    tasks.stop_tasks_db()


@pytest.fixture()
def tasks_db(tasks_db_session):  # task_db依赖了tasks_db_session,执行完tasks.delete_all()则tasks_db函数会teardown掉，不会一直跑
    """An empty tasks db."""
    tasks.delete_all()

# Reminder of Task constructor interface
# Task(summary=None, owner=None, done=False, id=None)
# summary is required
# owner and done are optional
# id is set by database


@pytest.fixture(scope='session')
def tasks_just_a_few():
    """All summaries and owners are unique."""
    return (
        Task('Write some code', 'Brian', True),
        Task("Code review Brian's code", 'Katie', False),
        Task('Fix what Brian did', 'Michelle', False))


@pytest.fixture(scope='session')
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