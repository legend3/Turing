"""Test the Task data type."""

from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


def test_asdict():
    """_asdict() should return a dictionary."""
    t_task = Task('do something', 'okken', True, 21)
    t_dict = t_task._asdict()  # 返回一个元素名与元素值键值对的字典
    print('\r',type(t_dict))
    print(t_dict)
    expected = {'summary': 'do something',
                'owner': 'okken',
                'done': True,
                'id': 21}
    assert t_dict == expected


def test_replace():
    """replace() should change passed in fields."""
    t_before = Task('finish book', 'brian', False)
    t_after = t_before._replace(id=10, done=True)#根据元素名替换元素值
    print('\r',type(t_after))
    print(t_after)
    t_expected = Task('finish book', 'brian', True, 10)
    assert t_after == t_expected
