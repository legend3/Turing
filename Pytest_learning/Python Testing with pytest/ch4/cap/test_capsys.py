import sys
import pytest
import random


def greeting(name):
    print('Hi, {}'.format(name))


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


def yikes(problem):
    print('YIKES! {}'.format(problem), file=sys.stderr)  # 将内容输入到标准错误对象中;file=sys.stderr改变print输出内容，默认为sys.stdout


def test_yikes(capsys):
    yikes('Out of coffee!')
    out, err = capsys.readouterr()
    assert out == ''
    assert 'Out of coffee!' in err  # 判断是否在标准错误对象中


'''
pytest通常捕获来自测试和被测试代码的输出。这包括打印语句。
只有在完整的测试会话完成之后，才会显示捕获的输出，用于失败测试.-s选项关闭此功能，并在测试运行时将输出发送到stdout。
通常这工作得很好，因为它是您为了调试失败而需要看到的失败测试的输出。
但是，您可能希望允许一些输出通过默认的pytest输出捕获，以便在不打印所有内容的情况下打印一些内容。
你可以用capsys这样做。可以使用capsys.disabled()临时让输出通过捕获机制。
'''


def test_capsys_disabled(capsys):
    with capsys.disabled():
        print('\nalways print this')  # 在没有-s时也可以输出的内容
    print('normal print, usually captured')  # 需要-s才能输出的(正常print)内容


@pytest.mark.parametrize('i', range(40))
def test_for_fun(i, capsys):
    if random.randint(1, 10) == 2:
        with capsys.disabled():
            sys.stdout.write('F')
