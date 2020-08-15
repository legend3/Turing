"""Demonstrate -lf and -ff adn --cache-show with failing tests."""

import pytest
from pytest import approx


testdata = [
    # x, y, expected
    (1.01, 2.01, 3.02),
    (1e25, 1e23, 1.1e25),
    (1.23, 3.21, 4.44),
    (0.1, 0.2, 0.3),
    (1e25, 1e24, 1.1e25)
]


@pytest.mark.parametrize("x,y,expected", testdata)
def test_a(x, y, expected):
    '''您可以在命令行上指定测试用例：pytest -q "test_few_failures.py::test_a[1e+25-1e+23-1.1e+25]"'''
    """Demo approx()."""
    sum_ = x + y
    assert sum_ == approx(expected)

