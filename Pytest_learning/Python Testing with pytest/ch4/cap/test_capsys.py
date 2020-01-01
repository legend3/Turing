"""
capsys
内建装置提供了两个功能:它允许您从某些代码中检索stdout和stderr，并暂时禁用输出捕获。
让我们来看看检索stdout和stderr。假设您有一个将问候语打印到stdout的函数"""

import sys
import pytest
import random


def greeting(name):
    print('Hi, {}'.format(name))


# 捕获greeting(name)函数被调用的所有信息
def test_greeting(capsys):
    greeting('Earthling')
    '''返回值是自函数开始或最后一次调用以来捕获的任何值'''
    out, err = capsys.readouterr()  # 通过capsys捕获被调用函数的输出内容stdout、stderr
    assert out == 'Hi, Earthling\n'
    assert err == ''

    greeting('Brian')
    greeting('Nerd')
    out, err = capsys.readouterr()
    assert out == 'Hi, Brian\nHi, Nerd\n'
    assert err == ''


# 只输出错的信息
def yikes(problem):
    print('YIKES! {}'.format(problem), file=sys.stderr)  # 将内容输入到标准错误对象中;file=sys.stderr改变print输出内容，默认为sys.stdout


def test_yikes(capsys):
    yikes('Out of coffee!')
    out, err = capsys.readouterr()
    assert out == ''  # 只打印错误信息
    assert 'Out of coffee!' in err  # 判断是否在标准错误对象中


'''
pytest通常捕获来自测试和被测试代码的输出。这包括打印语句。
只有在完整的测试会话完成之后，才会显示捕获的输出，用于失败测试.-s选项关闭此功能，并在测试运行时将输出发送到stdout。
通常这工作得很好，因为它是您为了调试失败而需要看到的失败测试的输出。
!!!但是，您可能希望允许一些输出通过默认的pytest输出捕获，以便在不打印所有内容的情况下打印一些内容。
你可以用capsys这样做。
可以使用capsys.disabled()临时让输出通过捕获机制。
'''


def test_capsys_disabled(capsys):
    with capsys.disabled():  # 临时关闭capsys捕获(这样正常输出print才会打印出来，不然只能加命令选项-s)
        print('\nalways print this')  # 在没有-s时也可以输出的内容
    print('normal print, usually captured')  # 需要-s才能输出的(正常print)内容


@pytest.mark.parametrize('i', range(40))
def test_for_fun(i, capsys):
    if random.randint(1, 10) == 2:
        with capsys.disabled():
            sys.stdout.write('F')
            # print("F", end="")


"""正如您所看到的，无论是否捕获输出，都要打印它，因为它是从一个with capsys.disabled()块中打印出来的。
另一个print语句只是一个普通的print语句，所以普通的print，
通常只有在我们传递-s标志时才会被看到，这是-capture=no，关闭输出capture的快捷方式。"""