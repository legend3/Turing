import pytest


@pytest.fixture()
def y():
    print("Ԥ���ɹ���")
    x = yield 1
    print('x ->', x)

def test_01(y):
    assert True