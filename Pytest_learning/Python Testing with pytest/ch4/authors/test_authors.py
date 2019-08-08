"""Some tests that use temp data files."""
import json

'''
author_file.json测试数据文件适用于多个测试，如果为两个测试都重新创建它就没有意义了。
'''
def test_brian_in_portland(author_file_json):
    """A test that uses a data file."""
    with author_file_json.open() as f:
        authors = json.load(f)#json-->字段
    assert authors['Brian']['City'] == 'Portland'


def test_all_have_cities(author_file_json):
    """Same file is used for both tests."""
    with author_file_json.open() as f:#执行author_file_json.open()返回值赋值与f，在执行authors = json.load(f)，如果成功不报异常，反之亦然。
        authors = json.load(f)
    for a in authors:
        assert len(authors[a]['City']) > 0
