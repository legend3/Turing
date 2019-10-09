#  ecoding utf8
"""
This module defines multiply(a, b) and divide(a, b).

>>> import unnecessary_math as um

Here's how you use multiply:

>>> um.multiply(4, 3)
12
>>> um.multiply('a', 3)
'aaa'


Here's how you use divide:

>>> um.divide(10, 5)
2.0
"""

'''
1.
（不是fixture内置）doctest模块会搜索那些看起来像是python交互式会话中的代码片段，然后尝试执行并验证结果。

2.
*有两个地方可以放doctest测试用例，一个位置是模块的最开头，另一个位置是函数声明语句的下一行（就像上面的例子这样）。
除此之外的其它地方不能放，放了也不会执行。

3.
那个verbose参数，如果设置为True则在执行测试的时候会输出详细信息。
默认是False，表示运行测试时，只有失败的用例会输出详细信息，成功的测试用例不会输入任何信息。
'''


def multiply(a, b):
    """
    Returns a multiplied by b.

    >>> um.multiply(4, 3)
    12
    >>> um.multiply('a', 3)
    'aaa'
    """
    return a * b


def divide(a, b):
    """
    Returns a divided by b.

    >>> um.divide(10, 5)
    2.0
    """
    return a / b


def multiply(a, b):
    """
    >>> multiply(4, 3)
    12
    >>> multiply('a', 3)
    'aaa'
    """
    return a * b


# 补充：
if __name__ == '__main__':
    import doctest  # 不是fixtures内置的doctest
    doctest.testmod(verbose=True)
