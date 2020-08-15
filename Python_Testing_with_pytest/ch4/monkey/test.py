# encoding utf8
import os,sys
import cheese,copy

# def getssh():
#     print(os.path.expanduser("~admin"))
#     return os.path.join(os.path.expanduser("~admin"), '.ssh')
#
#
# def test_mytest(monkeypatch):
#     def mockreturn(path):
#         return '/abc'
#     monkeypatch.setattr(os.path, 'expanduser', mockreturn)
#     x = getssh()
#     assert x == '/abc\\.ssh'
#
#
# if __name__ == '__main__':
#     getssh()


def monkey_patch_dict(monkeypatch):
    cheese.write_default_cheese_preferences()
    defaults_before = copy.deepcopy(cheese._default_prefs)
    print(defaults_before)
    monkeypatch.setitem(cheese._default_prefs,'slicing',["1"])