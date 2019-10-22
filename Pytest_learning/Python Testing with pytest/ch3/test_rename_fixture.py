"""Demonstrate fixture renaming."""

import pytest

'''
如果需要找出lue的定义位置，可以添加pytest选项——fixture，并为测试提供文件名。
它列出了测试可用的所有fixture，包括已重命名的fixture
$ pytest --fixtures test_rename_fixture.py
'''
@pytest.fixture(name='lue')
def ultimate_answer_to_life_the_universe_and_everything():
    """Return ultimate answer."""
    return 42


def test_everything(lue):
    """Use the shorter name."""
    assert lue == 42  # 与ultimate_answer_to_life_the_universe_and_everything等效；使用使用列表fixture的返回值
