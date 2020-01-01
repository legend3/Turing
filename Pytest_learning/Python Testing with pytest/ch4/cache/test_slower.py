"""演示---clear-cache"""

import datetime
import pytest
import random
import time

'''

缓存可以不仅仅用于——lf和——ff。
你可以利用-clear-cache，在(每次)会话之前清除缓存。

场景：
利用cacha存储上一次运行的值,让我们创建一个fixture，它记录测试花费的时间，存储（运行）次数，
在下一次运行时，报告一个(如果)测试花费的时间是上次的两倍的错误

缓存fixture的接口很简单
cache.get(key, default)
cache.set(key, value)


按照惯例，key名以应用程序或插件的名称开头，后面跟一个/，然后继续用/分隔key名的各个部分。
存储的值可以是任何可转换为json的值，因为这就是.cache目录中表示值的方式

请求对象一般习惯于获取nodeid在key中使用。
nodeid是一个惟一的标识符(代表一次测试，例如duration\test_slower.py__test_slow_stuff[0]中的test_slower.py__test_slow_stuff[0])，
它甚至可以用于参数化测试

——test_slower.py案例场景，各自独立的'函数范围'间对比判断
'''
@pytest.fixture(autouse=True)
def check_duration(request, cache):
    key = 'duration/' + request.node.nodeid.replace(':', '_')  # 2.命名创建缓存文件(获取nodeid)，必须是带有一个/分隔值。
                                                                # 通常第一个名称是插件或应用程序的名称(此处为第一部分！)
    # nodeid's can have colons
    # keys become filenames within .cache
    # replace colons with something filename safe
    start_time = datetime.datetime.now()
    yield
    stop_time = datetime.datetime.now()
    this_duration = (stop_time - start_time).total_seconds()
    last_duration = cache.get(key, None)  # 1.获取缓存key;如果尚未缓存任何值或无法读取该值则返回指定的默认值None
    cache.set(key, this_duration)  # 保存value(此处为this_duration;必须是基本python类型的任何组合，
                                    # 包括嵌套类型，如字典列表)到给定的key值(例如，duration\test_slower.py__test_slow_stuff[0])
    if last_duration is not None:
        errorstring = "test duration over 2x last duration"
        assert this_duration <= last_duration * 2, errorstring  # this_duration本次运行花费时间；
                                                                # last_duration上次的cache的value值;对比前、后两次

# 因为您可能不想为此编写一堆测试，所以我使用随机和参数化来轻松地生成一些睡眠时间随机的测试，
# 这些测试的睡眠时间都小于一秒。让我们看看它运行了几次:
@pytest.mark.parametrize('i', range(5))
def test_slow_stuff(i):
    time.sleep(random.random())
