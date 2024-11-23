"""前言: 
monkey补丁是运行时对类或模块的动态修改。在测试期间,
monkey补丁是接管被测试代码的部分运行时环境并将输入依赖项或输出依赖项替换为更方便测试的对象或函数的一种方便方法。
monkeypatch内建装置允许您在单个测试的上下文中执行此操作。当测试结束时,不管是否通过,原始的未修补程序都会被恢复,
撤销由修补程序更改的所有内容。
这都是手把手的,直到我们跳到一些例子。

monkeypath主要有以下几个用处: (个人理解——"临时修改";monkeypatch像一个全局的管理者,
                                可随时随地对任何环境进行修改 配置;只是修改了执行时的代码,不破坏被调用的原代码)
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
• syspath_prepend(path): Prepend path to sys.path, which is Python`s list of import locations.(您可以使用monkeypatch.syspath_prepend()来预先设置存根版本的目录,被测试的代码将首先找到存根版本)
• chdir(path): Change the current working directory.(chdir(path)在测试期间更改当前工作目录。
这对于测试命令行脚本和其他依赖于当前工作目录的实用程序非常有用。您可以设置一个临时目录,其中包含对脚本有意义的任何内容,然后使用monkeypatch.chdir (the_tmpdir)。)"""

import copy
import pathlib
import cheese


def test_def_prefs_full():
    # 默认cheese.py函数中指定的目录下运行    -- full_path:     C:\Users\Administrator
    cheese.write_default_cheese_preferences()
    expected = cheese._default_prefs
    actual = cheese.read_cheese_preferences()
    assert expected == actual


"""这样做的一个问题是,运行这个测试代码的任何人都会覆盖他们自己的cheese首选项文件。那不是很好。
如果用户有HOME设置(xxx用户根目录),！！！那么os.path.expanduser()将用户的~替换为用户的HOME里的环境变量。
让我们创建一个临时目录并重定向HOME指向新的临时目录:(变换用户,自动在用户根目录下创建 一个临时目录)

注释: HOME(的值): （默认情况下）为执行这个测试的临系统临时目录(Temp)的子目录临时目录;基本名称将是pytest-数字,
其中数字将随着每次测试运行而递增;此外,第3个以后的临时目录会被删除

可以利用命令选项--basetemp= 修改HOME默认路径
"""


def test_def_prefs_change_home(tmpdir, monkeypatch):
    # 1.调用执行cheese.write_default_cheese_preferences()函数前,
    # 2.利用monkeypath自动切换到任意系统(xxx用户)的根目录(Temp)的pytest临时目录的根目录下(默认: C:\Users\Administrator\AppData\Local\Temp\pytest-of-Administrator)——(自动适配任意系统(用户))
    """在本地计算机上分发测试时,pytest会为子进程配置临时目录根目录,以便所有临时数据都落在单个每个测试运行的临时目录根目录。"""
    # 3.临时修改目录路径运行(被)
    monkeypatch.setenv("HOME", tmpdir.mkdir("home"))
    cheese.write_default_cheese_preferences()
    expected = cheese._default_prefs
    actual = cheese.read_cheese_preferences()
    assert expected == actual


def test_def_prefs_change_expanduser(fake_home_dir, monkeypatch):
    # fake_home_dir = tmpdir.mkdir("home")  # 代表pytest临时根目录下,创建home目录
    fake_home_dir = pathlib.WindowsPath('C:/Users/Administrator/Desktop/home')
    fake_home_dir.mkdir(parents=True,exist_ok=True)  # 自定义目录路径

    """利用monkeypath(在运行时)对cheese文件下所有os.path的expanduser属性都会生效;如果涉及的方法(或文件)多就特别美妙了!"""
    monkeypatch.setattr(
        cheese.os.path, "expanduser", (lambda x: x.replace("~", str(fake_home_dir)))
    )
    # 等效;cheese.os.path.expanduser为target指定字符串会被import path解析,expanduser为属性名且修改expanduser属性值;
    # 记忆原有cheese.os.path.expanduser的值
    # monkeypatch.setattr("cheese.os.path.expanduser",
    #                     (lambda x: x.replace('~', str(fake_home_dir))))  # 设置expanduser属性,对os.path的expanduser进行修改
    cheese.write_default_cheese_preferences()
    expected = cheese._default_prefs
    actual = cheese.read_cheese_preferences()
    assert expected == actual


# 演示setattr(),修改属性(expanduser)
def test_def_prefs_change_defaults(tmpdir, monkeypatch):
    # write the file once
    fake_home_dir = tmpdir.mkdir("home")
    monkeypatch.setattr(
        cheese.os.path, "expanduser", (lambda x: x.replace("~", str(fake_home_dir)))
    )
    cheese.write_default_cheese_preferences()
    defaults_before = copy.deepcopy(cheese._default_prefs)

    # change the defaults （通过monkeypatch临时修改——演示setitem()）
    monkeypatch.setitem(cheese._default_prefs, "slicing", ["provolone"])
    monkeypatch.setitem(cheese._default_prefs, "spreadable", ["brie"])
    monkeypatch.setitem(cheese._default_prefs, "salads", ["pepper jack"])
    defaults_modified = cheese._default_prefs

    # write it again with modified defaults
    cheese.write_default_cheese_preferences()

    # read, and check
    actual = cheese.read_cheese_preferences()
    assert defaults_modified == actual
    assert defaults_modified != defaults_before
