"""Minimal Project Task Management.
告诉Python
该目录是一个包。该项目包含两种类型的_init_ .py文件:在src/目录下找到的文件和在tests/下找到的文件。py文件告诉Python该目录是一个包。当有人使用导入任务时，它还充当包的主接口。
它包含从api.py导入特定函数的代码，这样clic .py和我们的测试文件就可以访问像tasks.add()这样的包功能，而不必执行tasks.api.add()。
"""

from .api import (  # noqa: F401
    Task,
    TasksException,
    add,
    get,
    list_tasks,
    count,
    update,
    delete,
    delete_all,
    unique_id,
    start_tasks_db,
    stop_tasks_db
)

__version__ = '0.1.0'
