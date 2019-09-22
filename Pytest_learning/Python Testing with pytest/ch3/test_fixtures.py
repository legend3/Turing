"""Demonstrate simple fixtures."""

import pytest


@pytest.fixture()
def some_data():
    """Return answer to ultimate question."""
    return 42


def test_some_data(some_data):
    """Use fixture return value in a test."""
    assert some_data == 42


@pytest.fixture()
def some_other_data():
    """Raise an exception from fixture."""
    x = 43
    assert x == 42
    return x


'''
如果在fixture中发生断言(或任何异常)会发生什么?
判断是测试失败了还是测试所依赖的fixtrue失败了（测试出错）
1.
堆栈跟踪正确地显示了在fixture函数中发生的断言。
2.
另外，test_other_data报告的不是失败，而是错误。这种差别很大。
如果一个测试失败了，您就知道失败是在测试中发生的，而不是在它所依赖的任何fixture中发生的
'''


def test_other_data(some_other_data):
    """Try to use failing fixture."""
    assert some_data == 42


'''
fixture是存储用于测试的数据的好地方。你可以返回任何。这是一个返回混合类型元组的fixture
'''
@pytest.fixture()
def a_tuple():
    """Return something more interesting."""
    return (1, 'foo', None, {'bar': 23})


def test_a_tuple(a_tuple):
    """Demo the a_tuple fixture."""
    assert a_tuple[3]['bar'] == 32
