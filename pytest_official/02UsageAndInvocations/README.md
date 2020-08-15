# 获取有关版本，选项名称，环境变量的帮助

pytest --version＃显示从哪里导入pytest

pytest --fixtures＃显示可用的内置函数参数

pytest -h | --help＃在命令行和配置文件选项上显示帮助


# **使用与调用**

通过python -m pytest调用pytest

您可以从命令行通过Python解释器调用测试：(几乎等同于直接调用命令行脚本pytest [...]，除了通过python调用还会将当前目录添加到sys.path中!)

python -m pytest [...]

# 退出码

pytest的退出码
    运行pytest可能导致六个不同的退出代码：
        Exit code 0
            所有测试均已收集并成功通过
        Exit code 1
            测试已收集并运行，但有些测试失败
        Exit code 2
            测试执行被用户中断
        Exit code 3
            执行测试时发生内部错误
        Exit code 4
            pytest命令行用法错误
        Exit code 5
            没有收集测试
它们由_pytest.config.ExitCode枚举表示。 退出代码是公共API的一部分，可以使用以下方法直接导入和访问：
from pytest import ExitCode

# 在第一个（或N个）故障后停止 案例：test_Nfail.py

要在第一个（N）次失败后停止测试过程：

pytest -x＃第一次失败后停止

pytest --maxfail = 2＃两次失败后停止


# pytest -r
    1.-r标志可用于在测试会话结束时显示“简短的测试摘要信息”，从而使得在大型测试套件中轻松获得所有失败，跳过，xfails等的清晰画面。
    2.
        -ra -- 除了Pp（-r选项在其后接受许多字符，上面使用表示“除通行证外的所有字符”。）
        -rA -- 所有包括Pp
        -N -- 这可用于不显示任何内容（因为默认为fE）
    3.可以使用多个字符，例如，要仅查看失败和跳过的测试，可以执行：
        -rfs
    4.这是可以使用的可用字符的完整列表：
        f - failed

        E - error

        s - skipped

        x - xfailed

        X - xpassed

        p - passed

        P - passed with output

# pytest自带的debug (不好用！)

pytest -pdb 运行用例，在每当出现错误时，进入pdb模式

这将在每次失败（或KeyboardInterrupt）时调用Python调试器。 通常，您可能只想在第一个失败的测试中执行此操作，以了解特定的失败情况
pytest -x --pdb   # 在第一次失败时，请转到PDB，然后结束测试会话
pytest --pdb --maxfail=3    # 在前三个故障时下降到PDB

请注意，在发生任何故障时，异常信息都存储在sys.last_value，sys.last_type和sys.last_traceback中。 在交互式使用中，这使您可以使用任何调试工具进行事后调试。 也可以手动访问异常信息，例如：
>>> import sys
>>> sys.last_traceback.tb_lineno
42
>>> sys.last_value
AssertionError('assert result == "ok"',)

pytest --trace 在每个用例开始前，就进入pdb模式

# 分析测试执行时间
要获取最慢的10个测试持续时间的列表：

pytest --durations=10

默认情况下，除非在命令行上传递-vv，否则pytest不会显示太短的测试持续时间（<0.01s）
pytest -vv --durations=10

# 错误处理
Faulthandler标准模块可用于在segfault上或超时后转储Python跟踪。

此模块在pytest命令执行时会自动执行，除非在命令行添加: -p no:faulthandler
如果测试花费的时间超过X秒（在Windows上不可用），则faulthandler_timeout = X配置选项也可以用于dump所有线程的traceback。

此功能已从外部pytest-faulthandler插件集成，只有两个小区别：
(要取消-p no:faulthandler 而不是 --no-faulthandler)

（--faulthandler-timeout"命令行选项"已成为faulthandler_timeout"配置选项"。 仍然可以使用-o faulthandler_timeout = X从"命令"行进行配置。）
