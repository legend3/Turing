"""Testing the pytest-nice plugin.利用testdir(通过pytester)自动调用执行命令(带或不带选项)行，测试pytest-nice插件"""

import pytest

'''
testdir装置会自动创建一个临时目录来放置测试文件。它有一个名为makepyfile()的方法，允许我们放入测试文件的内容。在本例中，我们创建两个测试:一个通过，一个失败。
'''


def test_pass_fail(testdir):  # testdir在pytester打开后有用！！！

    # create a temporary pytest test module
    testdir.makepyfile("""
        def test_pass():
            assert 1 == 1

        def test_fail():
            assert 1 == 2
    """)

    '''
    我们使用testdir.runpytest()对新的测试文件运行pytest。如果需要，可以传入选项，然后可以进一步检查返回值(运行命令的结果)，其类型为RunResult.5
    '''
    # run pytest
    result = testdir.runpytest()  # result，0表示通过，1表示失败。

    # fnmatch_lines does an assertion internally
    # 搜索捕获的文本以查找匹配的行，所有的xxx.与所有的Fxxx
    result.stdout.fnmatch_lines([
        '*.F*',  # . for Pass, F for Fail
    ])

    '''通常，我查看stdout和ret，为了像手动一样检查输出，使用fnmatch_lines，传入一个我们希望在输出中看到的字符串列表，然后确保ret为0(传递会话)和1(失败会话)。
    传递给fnmatch_lines的字符串可以包含通配符。'''
    # make sure that that we get a '1' exit code for the testsuite
    assert result.ret == 1  # ret,pytester测试的返回值


# 我们可以使用sample_test作为已经包含我们的示例测试文件的目录
@pytest.fixture()
def sample_test(testdir):  # 测试插件的用例代码模板
    testdir.makepyfile("""
        def test_pass():
            assert 1 == 1

        def test_fail():
            assert 1 == 2
    """)
    return testdir


def test_with_nice(sample_test):
    result = sample_test.runpytest('--nice')    # 通过pytester自动调用命令选项
    result.stdout.fnmatch_lines(['*.O*', ])  # . for Pass, O for Fail，判断是否与插件事先定义的修改的状态一致
    assert result.ret == 1


def test_with_nice_verbose(sample_test):
    result = sample_test.runpytest('-v', '--nice')
    result.stdout.fnmatch_lines([
        '*::test_fail OPPORTUNITY for improvement*',
    ])
    assert result.ret == 1


def test_not_nice_verbose(sample_test):
    result = sample_test.runpytest('-v')
    result.stdout.fnmatch_lines(['*::test_fail FAILED*'])
    assert result.ret == 1


def test_header(sample_test):
    result = sample_test.runpytest('--nice')
    result.stdout.fnmatch_lines(['Thanks for running the tests.'])


def test_header_not_nice(sample_test):
    result = sample_test.runpytest()
    thanks_message = 'Thanks for running the tests.'
    assert thanks_message not in result.stdout.str()


def test_help_message(testdir):
    result = testdir.runpytest('--help')

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        'nice:',
        '*--nice*nice: turn FAILED into OPPORTUNITY for improvement',
    ])
