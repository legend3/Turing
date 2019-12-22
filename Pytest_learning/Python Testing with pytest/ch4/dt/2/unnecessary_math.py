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
pytest将每个带docstring的代码视为不同的测试。
所以顶部docstring中的import unnecessary_math as um仅将允许第一部分通过，但是函数文档字符串中的代码将失败；
所以要每个doctest中都>>> import unnecessary_math as um
'''


def multiply(a, b):
    """
    Returns a multiplied by b.

    >>> import unnecessary_math as um
    >>> um.multiply(4, 3)
    12
    >>> um.multiply('a', 3)
    'aaa'
    """
    return a * b


def divide(a, b):
    """
    Returns a divided by b.

    >>> import unnecessary_math as um
    >>> um.divide(10, 5)
    2.0
    """
    return a / b
