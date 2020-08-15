import pytest
import unnecessary_math

'''
告诉pytest将um名称添加到doctest_namespace中，并将其作为导入的unnecessary_math模块的值。
在conftest.py文件中有了这个，在这个conftest.py文件范围内找到的任何doctest都将定义um符号
'''
@pytest.fixture(autouse=True)  # 全局的doctest-modules
def add_um(doctest_namespace):
    doctest_namespace['um'] = unnecessary_math
