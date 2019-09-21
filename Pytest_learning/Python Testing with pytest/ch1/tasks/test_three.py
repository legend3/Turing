"""Test the Task data type."""

from collections import namedtuple

'''
导入pytest模块
参数：-m，标记需要同时执行的用例

Tuple还有一个兄弟，叫namedtuple。虽然都是tuple，但是功能更为强大。
对于namedtuple，你不必再通过索引值进行访问，你可以把它看做一个字典通过名字进行访问，只不过其中的值是不能改变的。
collections.namedtuple(typename, field_names, verbose=False, rename=False) 
返回一个具名元组子类 typename，其中参数的意义如下：
typename：元组名称
field_names: 元组中元素的名称
rename: 如果元素名称中含有 python 的关键字，则必须设置为 rename=True
verbose: 默认就好

test_member_access()测试演示如何通过名称而不是索引访问成员，这是使用namedtuples的主要原因之一！
'''
Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)#


def test_defaults():
    """Using no parameters should invoke defaults."""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2

def test_member_access():
    """Check .field functionality of namedtuple."""
    t = Task('buy milk', 'brian')
    assert t.summary == 'buy milk'
    assert t.owner == 'brian'
    assert (t.done, t.id) == (False, None)
