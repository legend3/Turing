import pytest


@pytest.fixture()
def y():
    print("Ô¤¼¤³É¹¦£¡")
    x = yield 1
    print('x ->', x)

def test_01(y):
    assert True