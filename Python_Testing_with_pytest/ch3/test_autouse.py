"""Demonstrate autouse fixtures."""

import pytest
import time

'''
当添加autouse设置为True时，在一个session内的所有的test都会自动调用这个fixture。
权限大，责任也大，所以用该功能时也要谨慎小心。
'''
@pytest.fixture(autouse=True, scope='session')
def footer_session_scope():
    """Report the time at the end of a session."""
    yield
    now = time.time()
    print('--')
    print('finished : {}'.format(time.strftime('%d %b %X', time.localtime(now))))
    print('-----------------')


@pytest.fixture(autouse=True)
def footer_function_scope():
    """Report test durations after each function."""
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start
    print('\ntest duration : {:0.4} seconds'.format(delta))  # {:0.3}占位符，表示至少占0.4个位


def test_1():
    """Simulate long-ish running test."""
    time.sleep(1)


def test_2():
    """Simulate slightly longer test."""
    time.sleep(1.23)
