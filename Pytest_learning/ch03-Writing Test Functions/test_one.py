import pytest
'''
测试一个异常用例会不会正常报出异常;
此时如果用assert话，测试代码本身就会报异常；
因此，此处我们使用   with pytest.raises()
'''

def test_add_raise():
    local = '测试一个会报ValueError异常的用例'
    str_to_change = '非数字字符不能转数字'
    with pytest.raises(ValueError):
        num = int(str_to_change)