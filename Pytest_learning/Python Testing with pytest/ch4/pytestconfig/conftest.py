"""
使用pytestconfig内置装置，您可以通过命令行参数和选项、配置文件、插件以及启动pytest的目录控制pytest如何运行。
pytestconfig装置是请求的快捷方式。配置，有时在pytest文档中称为pytest配置对象。要查看pytestconfig如何工作，
1.您将查看如何添加自定义命令行选项并从测试中读取选项值。2.您可以直接从pytestconfig中读取命令行选项的值，但是要添加该选项并让pytest解析它，
您需要添加一个hook函数。hook函数是另一种控制pytest行为的方法，并且在插件中经常使用，
我将在第5章，即插件中更详细地介绍它。但是，添加一个自定义命令行选项并从pytestconfig中读取它是非常常见的，因此我想在这里介绍它。
"""


def pytest_addoption(parser):  # pytest自带类
    '''添加自定义命令选项'''
    parser.addoption("--myopt", action="store_true",help="some boolean option")
    parser.addoption("--foo", action="store", default="bar",help="foo: bar or baz")
