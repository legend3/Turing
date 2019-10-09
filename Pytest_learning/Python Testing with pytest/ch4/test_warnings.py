import warnings
import pytest

'''
warnings标准库?

——recwarn内置fixtures用于验证由测试代码生成的警告
'''


def lame_function():
    warnings.warn("Please stop using this", DeprecationWarning)
    # rest of function


def test_lame_function(recwarn):
    lame_function()  # 调用执行被测方法(recwarn就开始收集warnings)
    assert len(recwarn) == 1
    '''recwarn值的作用类似于警告列表，列表中的每个警告都定义了一个类别、消息、文件名和lineno，如代码所示'''
    w = recwarn.pop()
    assert w.category == DeprecationWarning
    assert str(w.message) == 'Please stop using this'


def test_lame_function_2():
    '''除了recwarn之外，pytest还可以使用pytest.warns()检查警告:'''
    with pytest.warns(None) as warning_list:
        lame_function()
    print(warning_list)
    assert len(warning_list) == 1
    w = warning_list.pop()
    assert w.category == DeprecationWarning
    assert str(w.message) == 'Please stop using this'
