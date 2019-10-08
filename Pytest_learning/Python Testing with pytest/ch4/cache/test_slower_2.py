import pytest
import datetime
import random
import time
from collections import namedtuple

Duration = namedtuple('Duration', ['current', 'last'])

'''
test_slower_2.py案例，运行都在一个会话中
'''
@pytest.fixture(scope='session')  # 会话最先执行
def duration_cache(request):
    '''检测上一次的，没有也可读取空字典'''
    key = 'duration/testdurations'
    d = Duration({}, request.config.cache.get(key, {}))  # 给Duration的current、last传值(获取上一次缓存)
    print(d)
    print(request.config.cache.get(key, {}))
    yield d  # 将Duration传给check_duration()
    request.config.cache.set(key, d.current)


@pytest.fixture(autouse=True)  # 再调用自动
def check_duration(request, duration_cache):
    d = duration_cache  # 将Duration传给check_duration()
    nodeid = request.node.nodeid  # test_slower_2.py::test_slow_stuff[i]
    start_time = datetime.datetime.now()
    yield
    duration = (datetime.datetime.now() - start_time).total_seconds()
    d.current[nodeid] = duration  # 对'当前current'测试缓存中的nodeid赋值
    if d.last.get(nodeid, None) is not None:  # 如果有上一次(last)缓存,则用当前与其进行比较、判断
        errorstring = "test duration over 2x last duration"
        assert duration <= (d.last[nodeid] * 2), errorstring


@pytest.mark.parametrize('i', range(5))
def test_slow_stuff(i):
    time.sleep(random.random())


'''
cache.makedir(name)
返回具有给定名称的目录路径对象。如果目录还不存在，就会创建它。您可以使用它来管理诸如存储/检索跨测试会话的数据库转储之类的文件。
'''