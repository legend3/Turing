import copy
import cheese


'''
monkeypath主要有以下几个用处：(个人理解——"临时修改";monkeypatch像一个全局的管理者,可随时随地对任何环境进行修改 配置;只是修改了执行时的代码,不破坏被调用的原代码)
    在运行时替换方法、属性等
    在不修改第三方代码的情况下增加原来不支持的功能
    *在运行时为内存中的对象增加patch而不是在磁盘的源代码中增加

monkeypatch fixture提供了如下函数:
• setattr(target, name, value=<notset>, raising=True): Set an attribute.
• delattr(target, name=<notset>, raising=True): Delete an attribute.
• setitem(dic, name, value): Set a dictionary entry.
• delitem(dic, name, raising=True): Delete a dictionary entry.
• setenv(name, value, prepend=None): Set an environmental variable.
• delenv(name, raising=True): Delete an environmental variable.
• syspath_prepend(path): Prepend path to sys.path, which is Python’s list of import locations.(您可以使用monkeypatch.syspath_prepend()来预先设置存根版本的目录，被测试的代码将首先找到存根版本)
• chdir(path): Change the current working directory.(chdir(path)在测试期间更改当前工作目录。这对于测试命令行脚本和其他依赖于当前工作目录的实用程序非常有用。您可以设置一个临时目录，其中包含对脚本有意义的任何内容，然后使用monkeypatch.chdir (the_tmpdir)。)
'''


def test_def_prefs_full():
    # 默认cheese.py函数中指定的目录下运行
    cheese.write_default_cheese_preferences()
    expected = cheese._default_prefs
    actual = cheese.read_cheese_preferences()
    assert expected == actual


def test_def_prefs_change_home(tmpdir, monkeypatch):
    # 利用monkeypath针对HOME环境变量临时修改目录路径运行(被)
    monkeypatch.setenv('HOME', tmpdir.mkdir('home'))  # 根据HOME(HOME代表某一环境变量值,os.environ())创建临时home目录
    cheese.write_default_cheese_preferences()
    expected = cheese._default_prefs
    actual = cheese.read_cheese_preferences()
    assert expected == actual


def test_def_prefs_change_expanduser(tmpdir,monkeypatch):
    fake_home_dir = tmpdir.mkdir('home')
    # pathlib.WindowsPath('C:\\Users\\Administrator\\Desktop\\home').mkdir(parents=True,exist_ok=True)  # 自定义目录路径

    '''利用monkeypath(在运行时)对cheese文件下所有os.path的expanduser属性都会生效;如果涉及的方法(或文件)多就特别美妙了!'''
    monkeypatch.setattr(cheese.os.path, 'expanduser',
                        (lambda x: x.replace('~', 'C:\\Users\\Administrator\\Desktop\\home\\')))
    # 等效;cheese.os.path.expanduser为target指定字符串会被import path解析,expanduser为属性名且修改expanduser属性值;
    # 记忆原有cheese.os.path.expanduser的值
    # monkeypatch.setattr("cheese.os.path.expanduser",
    #                     (lambda x: x.replace('~', str(fake_home_dir))))  # 设置expanduser属性,对os.path的expanduser进行修改
    cheese.write_default_cheese_preferences()
    expected = cheese._default_prefs
    actual = cheese.read_cheese_preferences()
    assert expected == actual


def test_def_prefs_change_defaults(tmpdir, monkeypatch):
    # write the file once
    fake_home_dir = tmpdir.mkdir('home')
    # monkeypatch.setattr(cheese.os.path, 'expanduser',
    #                     (lambda x: x.replace('~', str(fake_home_dir))))
    monkeypatch.setattr(cheese.os.path, 'expanduser',
                        (lambda x: x.replace('~', 'C:\\Users\\Administrator\\Desktop\\home\\')))
    cheese.write_default_cheese_preferences()
    defaults_before = copy.deepcopy(cheese._default_prefs)

    # change the defaults
    monkeypatch.setitem(cheese._default_prefs, 'slicing', ['provolone'])
    monkeypatch.setitem(cheese._default_prefs, 'spreadable', ['brie'])
    monkeypatch.setitem(cheese._default_prefs, 'salads', ['pepper jack'])
    defaults_modified = cheese._default_prefs

    # write it again with modified defaults
    cheese.write_default_cheese_preferences()

    # read, and check
    actual = cheese.read_cheese_preferences()
    assert defaults_modified == actual
    assert defaults_modified != defaults_before
