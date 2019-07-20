import pytest

'''
导入pytest模块
参数：-m，标记需要执行的用例
'''
def add(x,y):
    return x+y

def test_add1():
    assert add(1,2) ==  3,"add(1,2)错误！"

# @pytest.mark.demo01
def test_add2():
    assert add(2,2) ==  3,"add(2,2)错误！"