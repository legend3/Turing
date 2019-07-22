"""Minimal Project Task Management.
告诉Python
该目录是一个包。它还充当到。的主接口;
当有人使用导入任务时进行打包。它包含特定于导入的代码
比如task .add()而不是必须执行task .api.add()。
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
