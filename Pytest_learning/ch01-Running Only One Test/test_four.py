from collections import namedtuple
'''
1.Tuple还有一个兄弟，叫namedtuple。虽然都是tuple，但是功能更为强大。
对于namedtuple，你不必再通过索引值进行访问，你可以把它看做一个字典通过名字进行访问，只不过其中的值是不能改变的。

2.创建了一个User类，并且拥有3个属性name,age和sex。默认创建Task类对象的时候，所有属性都需要赋值。
'''
Task = namedtuple('Task',['summary','owner','done','id'])
Task.__new__.__defaults__ = (None,None,False,None)

def test_asdict():
    """_asdict() should return a dictionary."""
    t_task = Task('do something', 'okken', True, 21)
    t_dict = t_task._asdict()
    expected = {'summary': 'do something',
    'owner': 'okken',
    'done': True,
    'id': 21}
    assert t_dict == expected#判断实践值与期望值是否相等

def test_replace():
    """replace() should change passed in fields."""
    t_before = Task('finish book', 'brian', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'brian', True, 10)
    assert t_after == t_expected