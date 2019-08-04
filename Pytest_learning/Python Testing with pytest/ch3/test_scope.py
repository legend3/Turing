"""Demo fixture scope."""

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
    print("我是mofule")

@pytest.fixture(scope='session')
def sess_scope():
    """A session scope fixture."""
    print("我是session")

@pytest.fixture(scope='class')
def class_scope():
    """A class scope fixture."""
    print("我是class")

def test_1(sess_scope, mod_scope, func_scope):
    """Test using session, module, and function scope fixtures."""
    print("函数1")


def test_2(sess_scope, mod_scope, func_scope):
    """Demo is more fun with multiple tests."""
    print("函数2")

'''
使用usefixture几乎与在测试方法参数列表中指定fixture名称相同。
唯一的区别是，测试只要在参数列表中指定fixture的就能使用Fixture的返回值。
而usefixtures标注的的测试不能使用fixture的返回值。
'''
@pytest.mark.usefixtures('class_scope')#指定fixture的作用域为class
class TestSomething():
    """Demo class scope fixtures."""

    def test_3(self):
        """Test using a class scope fixture."""
        print("函数3")

    def test_4(self):
        """Again, multiple tests are more fun."""
        print("函数4")
