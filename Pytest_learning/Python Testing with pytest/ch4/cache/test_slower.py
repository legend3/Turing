import datetime
import pytest
import random
import time

'''
缓存可以不仅仅用于——lf和——ff。
*让我们创建一个fixture，它记录测试花费的时间，存储（运行）次数，
在下一次运行时，报告一个(如果)测试花费的时间是上次的两倍的错误

按照惯例，key名以应用程序或插件的名称开头，后面跟一个/，然后继续用/分隔key名的各个部分。
存储的值可以是任何可转换为json的值，因为这就是.cache目录中表示值的方式

请求对象一般习惯于获取在键中使用的nodeid。nodeid是一个惟一的标识符，它甚至可以用于参数化测试
'''
@pytest.fixture(autouse=True)
def check_duration(request, cache):
    key = 'duration/' + request.node.nodeid.replace(':','_')
    # print('duration/' + request.node.nodeid)  # duration/test_slower.py::test_slow_stuff[i]
    # nodeid's can have colons
    # keys become filenames within .cache
    # replace colons with something filename safe
    start_time = datetime.datetime.now()
    yield
    stop_time = datetime.datetime.now()
    this_duration = (stop_time - start_time).total_seconds()
    last_duration = cache.get(key, None)  # (命名last_duration作为本次cache的变量)存储这次运行的nodeid到cache中key值
    cache.set(key, this_duration)  # 存储这次执行花费的时间到cacha中value值
    if last_duration is not None:
        errorstring = "test duration over 2x last duration"
        assert this_duration <= last_duration * 2, errorstring  # this_duration本次运行花费时间；last_duration上次的cache的value值;
                                                                # 对比前、后两次


@pytest.mark.parametrize('i', range(5))
def test_slow_stuff(i):
    time.sleep(random.random())
