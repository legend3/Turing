"""Demonstrate tmpdir_factory."""

import json
import pytest

'''
author_file_json() fixture创建一个名为data的临时目录，并创建一个名为author_file的文件。数据目录中的json。
然后它将python_author_data字典编写为json。因为这是一个module范围fixture，所以json文件只会为每个使用它进行测试的模块创建一次
'''
@pytest.fixture(scope='module')
def author_file_json(tmpdir_factory):
    """Write some authors to a data file."""
    python_author_data = {
        'Ned': {'City': 'Boston'},
        'Brian': {'City': 'Portland'},
        'Luciano': {'City': 'Sau Paulo'}
    }

    file = tmpdir_factory.mktemp('data').join('author_file.json')
    print('file:{}'.format(str(file)))

    with file.open('w') as f:
        json.dump(python_author_data, f)#字典-->json
    return file
