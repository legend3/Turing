import warnings
import pytest

'''
——warnings标准库
    场景使用：Python 通过调用 warnings 模块中定义的 warn() 函数来发出警告。警告消息通常用于提示用户一些错误或者过时的用法，当这些情况发生时我们不希望抛出异常或者直接退出程序。
    警告消息通常写入 sys.stderr，对警告的处理方式可以灵活的更改，例如忽略或者转变为为异常。警告的处理可以根据警告类别，警告消息的文本和发出警告消息的源位置而变化。对相同源位置的特定警告的重复通常被抑制。
    
    操作环节：警告控制分为两个阶段：首先，警告被触发时，确定是否应该发出消息；接下来，如果要发出消息，则使用用户可设置的Hook来格式化和打印消息。
    
    是否发出消息：警告过滤器可以用来控制是否发出警告消息，警告过滤器是一些匹配规则和动作的序列。可以通过调用 filterwarnings() 将规则添加到过滤器，并通过调用 resetwarnings() 将其重置为默认状态。
    发出消息：警告消息的输出是通过调用 showwarning() 函数来完成的，其可以被覆盖；该函数的默认实现通过调用 formatwarning() 格式化消息，这也可以由自定义实现使用。
    
——recwarn内置fixtures用于验证由测试代码生成的警告
'''


def lame_function():
    warnings.warn("Please stop using this", DeprecationWarning)  # DeprecationWarning默认忽略
    # rest of function


def test_lame_function(recwarn):
    lame_function()  # 调用执行被测方法(recwarn就开始收集warnings)
    assert len(recwarn) == 1
    '''recwarn值的作用类似于警告列表，列表中的每个警告都定义了一个类别、消息、文件名和lineno，如代码所示'''
    w = recwarn.pop()
    print('\n',w)
    assert w.category == DeprecationWarning
    assert str(w.message) == 'Please stop using this'


def test_lame_function_2():
    '''除了recwarn之外，pytest还可以使用pytest.warns()检查警告'''
    # with pytest.warns(None) as warning_list:
    with warnings.catch_warnings(record=True) as warning_list:
        warnings.simplefilter('always')
        lame_function()
    print("\n",warning_list)
    assert len(warning_list) == 1
    w = warning_list.pop()
    assert w.category == DeprecationWarning
    assert str(w.message) == 'Please stop using this'


if __name__ == '__main__':
    # import doctest
    # doctest.testmod(verbose=True)
    warnings.filterwarnings('error')
    test_lame_function_2
    # try:
    #     warnings.warn(Warning())
    # except Warning:
    #     print('Warning was raised as an exception!')
