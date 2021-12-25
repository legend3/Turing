#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author: LEGEND
@since: 2020-06-10 00:11:46
@lastTime: 2020-06-10 01:16:19
@LastAuthor: Do not edit
@FilePath: \Turing\Pytest_learning\Python Testing with pytest\pytest_dependency\all\test_02\test_mod_02.py
@Description: 
    1.注意："pytest_dependency/tests1/test_01/test_mod_01.py::test_a"是跟pytest命令执行时的所在位置为根(工作)目录
    例如：此时depends依赖路径，因此pytest应在E:\workspace\Turing\Pytest_learning\Python Testing with pytest\pytest_dependency目录下执行
    2.再可以指定要执行哪个目录里的case，pytest -v .\all\
    
@version:
"""


# test_mod_02.py


import pytest
import os


# @pytest.mark.dependency()
# @pytest.mark.xfail(reason="deliberate fail")
# def test_a():
#     assert False


@pytest.mark.dependency(
                        depends=["test_01/test_mod_01.py::test_a","test_01/test_mod_01.py::test_c"]
                        , scope='session'  # 跨文件需要session作用域
                        , name="e"
                        )
@pytest.mark.parametrize('case', [1,2,3])
def test_e(case):
    if case != 3:
        print(case)
    else:
        pytest.skip("跳过，就会不被依赖！") # 发生skip就是skip掉后续依赖用例！！！


@pytest.mark.dependency(depends=['e'])
def test_f():
    print("ffff")
    
# @pytest.mark.dependency(
#     depends=["tests/test_mod_01.py::test_b", "tests/test_mod_02.py::test_e"],
#     scope='session'
# )
# def test_f():
#     pass

# @pytest.mark.dependency(·
#     depends=["tests/test_mod_01.py::TestClass::test_b"],
#     scope='session'
# )
# def test_g():
#     pass


# if __name__ == '__main__':
#     print("路径：", os.path.split(os.path.abspath(__file__))[0].split('pytest_dependency\\')[1].replace("\\", "/"))
