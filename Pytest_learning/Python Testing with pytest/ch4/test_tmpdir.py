'''
——前沿
重用公共fixture是一个好主意，pytest开发人员在pytest中包含了一些常用的fixture。
在第59页的“更改任务项目fixture的范围”中，您已经看到任务项目使用tmpdir和tmpdir_factory。
*您将在本章中更详细地了解它们。pytest预先打包的内置fixture可以帮助您在测试中轻松且一致地做一些非常有用的事情。
例如，除了处理临时文件之外，pytest还包含内置fixture来访问命令行选项、测试会话之间的通信、验证输出流、修改环境变量和查询警告。
内建fixture是pytest核心功能的扩展。现在让我们一个接一个地看看几个最常用的建筑固定装置。

tmpdir与tmpdir_factory的意义
使用tmpdir和tmpdir_factory, tmpdir和tmpdir_factory内置fixture用于在测试运行之前创建一个临时文件系统目录，并在测试完成时删除该目录。
在Tasks项目中，我们需要一个目录来存储MongoDB和TinyDB使用的临时数据库文件。
但是，由于我们希望使用不能在测试会话之后存活下来的临时数据库进行测试，所以我们使用tmpdir和tmpdir_factory来为我们创建和清理目录。报告。

用例说明：
从tmpdir返回的值是py.path.local类型的对象。这似乎是我们需要的所有临时目录和文件。然而，有一个问题。
因为tmpdir fixture被定义为函数作用域，所以不能使用tmpdir创建文件夹或文件，*这些文件夹或文件的驻留时间应该超过一个测试函数。
对于范围不包括函数(类、模块、会话)的fixture，可以使用tmpdir_factory。

1.tmpdir
如果您正在测试读取、写入或修改文件的内容，您可以使用它
tmpdir用于创建单个测试使用的文件或目录.
2.tmpdir_factory
当您想为许多测试设置一个目录时,可以使用tmpdir_factory，
tmpdir fixture具有功能范围，tmpdir_factory fixture具有会话
范围。需要临时目录或文件的任何单个测试
单个测试可以使用tmpdir。对于正在设置的fixture也是如此
应该为每个测试函数重新创建的目录或文件。
tmpdir_factory fixture很像tmpdir，但是它有一个不同的接口。正如在指定Fixture作用域中所讨论的，在第56页，函数作用域Fixture为每个测试函数运行一次，模块作用域Fixture为每个模块运行一次，类作用域Fixture为每个类运行一次，测试作用域Fixture为每个会话运行一次。
因此，在会话范围fixture中创建的资源具有整个会话的生命周期。


'''

def test_tmpdir(tmpdir):#tmpdir只能保持test_tmpdir(函数范文)的执行
    # tmpdir already has a path name associated with it
    # join() extends the path to include a filename
    # the file is created when it's written to
    a_file = tmpdir.join('something.txt')

    # print(a_file)
    # you can create directories
    a_sub_dir = tmpdir.mkdir('anything')
    # print(a_sub_dir)
    # you can create files in directories (created when written)
    another_file = a_sub_dir.join('something_else.txt')
    # this write creates 'something.txt'
    a_file.write('contents may settle during shipping')
    # this write creates 'anything/something_else.txt'
    another_file.write('something different')
    # you can read the files as well
    assert a_file.read() == 'contents may settle during shipping'
    assert another_file.read() == 'something different'
#和test_tmpdir各自在不同的tmpdir函数范围
def test_tmpdir2(tmpdir):#tmpdir只能保持test_tmpdir(函数范文)的执行
    # tmpdir already has a path name associated with it
    # join() extends the path to include a filename
    # the file is created when it's written to
    a_file = tmpdir.join('something.txt2')

    # print(a_file)
    # you can create directories
    a_sub_dir = tmpdir.mkdir('anything2')
    # print(a_sub_dir)
    # you can create files in directories (created when written)
    another_file = a_sub_dir.join('something_else.txt2')
    # this write creates 'something.txt'
    a_file.write('contents may settle during shipping2')
    # this write creates 'anything/something_else.txt'
    another_file.write('something different2')
    # you can read the files as well
    assert a_file.read() == 'contents may settle during shipping2'
    assert another_file.read() == 'something different2'

def test_tmpdir_factory(tmpdir_factory):#使用tmpdir_factory使test_tmpdir_factory、test_tmpdir_factory2....都在同一个目录同一个会话中
    # you should start with making a directory
    # a_dir acts like the object returned from the tmpdir fixture
    a_dir = tmpdir_factory.mktemp('mydir')

    '''
    这个基本目录依赖于系统和用户，并且pytest-NUM会随着每个会话的递增而变化。
    在会话之后，基本目录将被单独保留，但是pytest将清理它们，并且只在系统上保留最近的几个临时基本目录，如果您需要在测试运行之后检查文件，这是非常棒的。
    
    如果需要，还可以使用pytest ——basetemp=mydir指定自己的基本目录
    '''
    # base_temp will be the parent dir of 'mydir'
    # you don't have to use getbasetemp()
    # using it here just to show that it's available
    base_temp = tmpdir_factory.getbasetemp()
    print('base:', base_temp)

    # the rest of this test looks the same as the 'test_tmpdir()'
    # example except I'm using a_dir instead of tmpdir

    a_file = a_dir.join('something.txt')#直接用a_dir，好似在tmpdir_factory会话范围内使用tmpdir(创建文件)
    a_sub_dir = a_dir.mkdir('anything')
    another_file = a_sub_dir.join('something_else.txt')

    a_file.write('contents may settle during shipping')
    another_file.write('something different')

    assert a_file.read() == 'contents may settle during shipping'
    assert another_file.read() == 'something different'
#和test_tmpdir_factory都在同一个会话范围内
def test_tmpdir_factory2(tmpdir_factory):  # 使用tmpdir_factory使test_tmpdir_factory、test_tmpdir_factory2....都在同一个目录同一个会话中
    # you should start with making a directory
    # a_dir acts like the object returned from the tmpdir fixture
    a_dir2 = tmpdir_factory.mktemp('mydir2')

    # base_temp will be the parent dir of 'mydir'
    # you don't have to use getbasetemp()
    # using it here just to show that it's available
    base_temp = tmpdir_factory.getbasetemp()
    print('base:', base_temp)

    # the rest of this test looks the same as the 'test_tmpdir()'
    # example except I'm using a_dir instead of tmpdir

    a_file = a_dir2.join('something.txt')  # 直接用a_dir，好似在tmpdir_factory会话范围内使用tmpdir(创建文件)
    a_sub_dir = a_dir2.mkdir('anything')
    another_file = a_sub_dir.join('something_else.txt')

    a_file.write('contents may settle during shipping')
    another_file.write('something different')

    assert a_file.read() == 'contents may settle during shipping'
    assert another_file.read() == 'something different'