"""Demo fixture scope.演示作用范围Demo"""

import pytest

'''
Specifying Fixture Scope：指定Fixture作用域
fixture包含一个名为scope的可选参数，该参数控制设置和拆卸fixture的频率。fixture()的作用域参数可以包含函数、类、模块或会话的值。
默认范围是function。
到目前为止，tasks_db fixture和所有fixture都没有指定作用域。因此,它们是功能范围固定装置。

scope='function'为每个测试函数运行一次。setup部分在使用Fixtures进行每次测试之前运行。yield执行开始执行（真正的）测试，teardown部分在每次测试之后使用Fixtures运行。这是在没有指定范围参数时使用的默认范围。
scope='class'为每个测试类运行一次，不管类中有多少测试方法。
scope='module'每个模块运行一次，不管模块中有多少测试函数、方法或其他fixture使用它。
scope='session'每个会话运行一次。使用会话范围fixture的所有测试方法和函数共享一个设置和拆卸调用。

setup执行顺序：session、module、class、function
tesardown执行顺序：function、class、module、session

fuction-->class-->module-->session
'''
@pytest.fixture(scope='function')
def func_scope():
    """A function scope fixture."""
    print("我是function")


@pytest.fixture(scope='module')
def mod_scope():
    """A module scope fixture."""
    # print("我是mofule")
    return [1,'2']

@pytest.fixture(scope='session')
def sess_scope():
    """A session scope fixture."""
    print("我是session")
    return 1


@pytest.fixture(scope='class')
def class_scope():
    """A class scope fixture."""
    print("我是class")


def test_1(sess_scope, mod_scope, func_scope):  # (同级，先后关系）
    """Test using session, module, and function scope fixtures."""
    print("函数1")  # test_1执行完，退出function范围
    print("mod_scoped的返回值第一元素:",mod_scope[0])


def test_2(sess_scope, mod_scope, func_scope):  # 1.方法中都可以对添加的fixtrue返回值进行利用
    """Demo is more fun with multiple tests."""
    print("函数2")   # test_12执行完，退出function范围
    print("mod_scope的返回值第二元素:",mod_scope[1])


'''
1.
当用例需要调用fixture时，前面讲到可以直接在用例里加fixture参数，如果一个测试class都需要用到fixture，
每个用例都去传参，会比较麻烦，这个时候，
可以在class外面加usefixtures装饰器，让整个class都调用fixture
2.
使用usefixtures等于在测试方法参数列表中指定fixture名称。
*唯一的区别是:
    a.测试只要在参数列表中指定fixture的就能使用Fixture的返回值。
    b.usefixtures标注的的测试不能使用fixture的返回值!
    c.available fixtures:通过命令 pytest --fixtures [testpath]查询此包中有效的fixtures有哪些
'''
@pytest.mark.usefixtures('class_scope')  # 指定usefixture的作用域为class(类中所有方法都是class_scope作用域 )
class TestSomething():
    """Demo class scope fixtures."""

    def test_3(self):
        """Test using a class scope fixture."""
        # print("函数3",class_scope)  # 类中不能对添加的fixture的返回值进行利用

    def test_4(self):
        """Again, multiple tests are more fun."""
        print("函数4")


'''
补充说明：
叠加fixture
如果class用例需要同时调用多个fixture，可以使用@pytest.mark.usefixtures()叠加方式。
'''


@pytest.fixture(scope="module")
def first():
    print("第一步：操作aaa")
    return (1, 'foo', None, {'bar': 23})


@pytest.fixture(scope="module")
def second():
    print("第二步：操作bbb")


'''1.注意叠加顺序，先执行的放底层，后执行的放上层；都会对类中每个测试方法都fixtures()'''
# @pytest.mark.usefixtures("second")  # 后执行
# @pytest.mark.usefixtures("first")  # 先执行

'''2.字符串列表形式(方便)；都会对类中每个测试方法都fixtures()'''
@pytest.mark.usefixtures("first", "second")
class TestFix():
    def test_1(self):
        print("用例1")
        # print(first[0])  # 不能获取到usefixtrues的返回值
        assert 1 == 1

    def test_2(self):
        print("用例2")
        assert 2 == 2
