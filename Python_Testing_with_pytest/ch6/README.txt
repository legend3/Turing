# 配置汇总
pytest.ini  ——这是允许您更改默认行为的主要pytest Config文件
conftest.py ——这是一个本地插件，允许hook函数和fixture用于conftest.py文件所在的目录和所有子目录
__init__.py ——当放入每个测试子目录时，该文件允许您在多个测试目录中拥有相同的测试文件名
tox.ini ——这个文件类似于pytest.ini，但是(只是)为了tox。但是，您可以将pytest配置放在这里，而不是同时拥有一个tox.ini和一个pytest.ini文件，从而节省了一个配置文件。
setup.cfg   ——如果您希望分发Python包(如任务)，这个文件将是您感兴趣的
                这是一个ini文件格式的文件，它影响setup.py的行为。可以向setup.py中添加几行代码来运行python setup.py test，
                并让它运行所有的pytest测试。
                如果您正在分发一个包，您可能已经有了setup.cfg文件，您可以使用该文件来存储pytest配置

# 使用pytest -help列出有效的ini文件选项
    添加命令选项
    改变命令选项，可以在pytest.ini文件中添加经常频繁使用的命令选项；例如：
        [pytest]
        addopts = -rsxX -l --tb=short --strict
        -rsxX   告诉pytest报告skipped, xfailed,xpassed的原因
        -l      告诉pytest用stacktrace报告每次失败的本地变量
        --tb=short  删除大量堆栈跟踪;会留下文件和行号
        --strict    如果mark没有在配置文件中注册，则不允许使用它们；例如：自定义的“smoke”、“get”

#  (上述)配置文件列表不是常量。插件(和conftest.py文件)可以添加ini文件选项。添加的选项也将添加到pytest—help输出中！
    添加默认命令行选项：(pytest.ini)
        [pytest]
            addopts = -rsxX -l --tb=short --strict
    注册自定义"markers"以避免(自定义)标记错误:(pytest.ini)两种方式
        1.(conftest.py中)
            def pytest_configure(config):
              markers_list = ["smoke","get"]
              for marker in markers_list:
                  config.addinivalue_line("markers",marker)
         2.
            [pytest]
            markers =
                smoke: Run the smoke test functions for tasks project
                get: Run the test functions that test tasks.get()
# 添加默认命令选项
        ch6\a与ch6\b对比：
            a无pytest.ini，所以默认没有--strict     任何拼写错误或未注册的标记都会显示为错误
            b添加pytes.ini，而且添加了默认开启--strict]

# 最小pytest版本设置:(pytest.ini)
        [pytest]
        minversion = 5.3.2

# pytest对项目扫描(鉴于norecursedirs告诉pytest不要看哪里，但是testpaths告诉pytest要看哪里)

    避免pytest递归无需的目录设置<可以使用norecursedirs缩小pytest的搜索范围>:(pytest.ini)
        # content of pytest.ini
        [pytest]
        norecursedirs = .* venv src *.egg dist build  # 指定pytest忽略某些目录(.开头的文件、目录 venv目录 src目录 egg结尾的目录 dist目录 build目录)
        [pytest]
        norecursedirs = .svn _build tmp*
        这将告诉pytest不要递归地进入典型的subversion或sphinx-build目录或任何tmp前缀目录

        *指定（只）测试目录的位置
            testspaths,是一个目录列表，它涉及于要查找测试的根目录(都根据某个'根目录'——应用场景情况)。它只在目录、文件或nodeid没有作为参数（不会被其他调用，“写死的”）给出的情况下使用
                [pytest]
                testpaths = tests # (pytest.ini所在目录为根目录，testpath根据根目录的相对目录设置) 只要你开始对tasks_proj项目pytest进行测试，pytest将只对task_proj/tests下的测试进行;
                    缺点：不适合做交互式的测试(testspath对于来自文件系统不同部分的交互式测试帮助不大)
                    优点:适合做持续集成测试或tox(在这些情况下，您知道根目录将是固定的，您可以列出相对于固定根目录的目录。在这些情况下，您确实需要缩短测试时间，因此减少一些测试发现是非常棒的)
                    总结:（同时使用testpaths和norecursedirs可能看起来很傻。但是，正如您所看到的，testspath对于来自文件系统不同部分的交互式测试帮助不大。
                    在这些情况下，norecursedirs可以提供帮助。另外，如果目录中的测试不包含测试，可以使用norecursedirs来避免这些情况。但实际上，在没有测试的测试中放置额外的目录又有什么意义呢?）

# 更改测试发现规则
    pytest标准的发现规则：
        1.从一个或多个目录开始。您可以在命令行上指定文件名或目录名。如果不指定任何内容，则使用当前目录
        2.递归查找测试模块所在的目录和所有子目录
        3.*文件名命名规则：(被)测试模块是一个文件名类似于test_*.py或*_test.py的文件
        4.*方法命名规则：在(被)测试模块中查找以test_开头的函数。
        5.*类命名规则：寻找以Test开头的类。在那些以test_开头但没有_init__方法的类中寻找方法
    修改标准发现规则：
        对于pytest和类，通常的测试发现规则是，如果一个类以Test*开头(类如:TestAdd类)，那么它就是一个潜在的测试类。该类也不能有一个_init__()函数。
        但是如果我们想将我们的测试类命名为<xxx>Test或<xxx>Suit?这就是python_classes的用武之地：
                # pytest.ini文件中
                [pytest]
                python_classes = *Test Test* *Suite
                从而，这使我们能够这样命名类:
                    class DeleteSuite():
                        def test_delete_1():
                        ...
                        def test_delete_2():
                        ...
                        ....
        同上，pytest和文件，
                # pytest.ini文件中
                [pytest]
                python_files = test_* *_test check_*
                 从而，这使我们能够这样命名文件:
                    check_login.py
       同上，pytest和方法，
                # pytest.ini文件中
                [pytest]
                python_functions = test_* check_*
                 从而，这使我们能够这样命名函数:
                    check_login()
#   避免文件名冲突dups与dups_fxed进行对比
    当不同子目录中出现相同文件名的，需要在各子目录中各自添加__init__.py
    因此，把__init__.py文件放进去，作为一个好习惯，就再也不要再担心了。