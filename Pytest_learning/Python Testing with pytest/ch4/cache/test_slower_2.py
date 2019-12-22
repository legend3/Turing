import pytest
import datetime
import random
import time
from collections import namedtuple

'''
——test_slower_2.py案例场景，归成一个会话中多次运行间的对比、判断
'''
Duration = namedtuple('Duration', ['current', 'last'])


@pytest.fixture(scope='session')  # 会话最先执行
def duration_cache(request):
    '''建立一个会话级别的key'''
    key = 'duration/testdurations'  # duration\testdurations contains:
    d = Duration({}, request.config.cache.get(key, {}))  # 给Duration的current、last传值(获取上一次缓存)
    yield d  # 将Duration传给check_duration()
    request.config.cache.set(key, d.current)  # 保存'当前'current测试到缓存(成为下一次测试的上一次)


@pytest.fixture(autouse=True)  # 再调用自动
def check_duration(request, duration_cache):
    '''针对会话key进行多个用例的运行对比'''
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
    '''被测用例'''
    time.sleep(random.random())


'''
cache.makedir(name)
返回具有给定名称的目录路径对象。如果目录还不存在，就会创建它。您可以使用它来管理诸如存储/检索跨测试会话的数据库转储之类的文件。

总结：
1.创建一个/开头的key
2.通过cache.get()获取上一次缓存并传给key
3.把当前的测试结果(花费时间)通过cache.set()传给key,作为下一次测试作对比、判断的'上一次缓存'

'''