import pytest

"""演示调用pytestconfig中(内置、自定义)的命令选项"""


def test_option(pytestconfig):
    """读取命令行选项的值"""
    print('"foo" set to:', pytestconfig.getoption('foo'))  # 方式一
    print('"myopt" set to:', pytestconfig.getoption('myopt'))


@pytest.fixture()
def foo(pytestconfig):
    return pytestconfig.option.foo  # 方式二


@pytest.fixture()
def myopt(pytestconfig):
    return pytestconfig.option.myopt


def test_fixtures_for_options(foo, myopt):
    """通过fixtures方式读取命令行选项的值"""
    print('"foo" set to:', foo)
    print('"myopt" set to:', myopt)


def test_pytestconfig(pytestconfig):
    print('args            :', pytestconfig.args)  # 方式三
    print('inifile         :', pytestconfig.inifile)
    print('invocation_dir  :', pytestconfig.invocation_dir)
    print('rootdir         :', pytestconfig.rootdir)
    print('-k EXPRESSION   :', pytestconfig.getoption('keyword'))
    print('-v, --verbose   :', pytestconfig.getoption('verbose'))
    print('-q, --quiet     :', pytestconfig.getoption('quiet'))
    print('-l, --showlocals:', pytestconfig.getoption('showlocals'))
    print('--tb=style      :', pytestconfig.getoption('tbstyle'))


def test_legacy(request):
    print('\n"foo" set to:', request.config.getoption('foo')) # 方式四
    print('"myopt" set to:', request.config.getoption('myopt'))
    print('"keyword" set to:', request.config.getoption('keyword'))
