import pytest

# @pytest.mark.demo01
def test_passing():
    print('测试是否会打印出来')
    assert (1,2,3,4,5,6) == (1,2,3,4,5,6)  # "不相等"