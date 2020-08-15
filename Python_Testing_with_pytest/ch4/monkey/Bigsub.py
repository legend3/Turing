import json
import ujson


def monkey_patch_json():
    json.__name__ = 'ujson'
    json.dumps = ujson.dumps
    json.loads = ujson.loads


monkey_patch_json()
print('Bigsub.py', json.__name__)
print(json.__name__)
#  导入sub文件,自动执行其代码
import sub