"""
Avoid test file name collision.

__init__.py files in test directories allow
test files in multiple directories to have the same
name in the same session.

See "Avoiding Filename Collisions" in Chapter 6 for
more information.

告诉上一个目录查找测试目录的根目录并查找pytest.ini文件。
"""
