pytest-xdist官网地址：【Home-page: https://github.com/pytest-dev/pytest-xdist】  

该pytest-xdist插件扩展了一些独特的测试执行模式pytest：  

测试运行并行化：如果有多个CPU或主机，则可以将它们用于组合测试运行。会加快运行速度  

--looponfail：在子进程中重复运行测试。每次运行之后，pytest会等待，直到项目中的文件发生更改，然后重新运行以前失败的测试。
重复此过程直到所有测试通过，之后再次执行完整运行。

多平台覆盖：您可以指定不同的Python解释器或不同的平台，并在所有平台上并行运行测试。 
在远程运行测试之前，pytest有效地将您的程序源代码“rsyncs”到远程位置。报告所有测试结果并显示给您的本地终端。您可以指定不同的Python版本和解释器。  
如果您想知道pytest-xdist如何在幕后工作，可以看这里【OVERVIEW】  


用parametrize来做参数化的时候 赋予了一个随机数据(random.chice() or time.time())  
ps：@pytest.mark.parametrize(‘new_url’, “http://www.{}.com”.format(random.chice(“abcdefg”)))  
上面这种写法是会出问题的 大概意思就是说 pytest-x-dist 在并发执行parametrize参数化的时候需要入参为静态数据  
具体参考：pytest-xdist并发过程及参数化说明  
然后解决方法就是把造随机数据的部分写入到函数里面 改动的话需要检查下这个接口有没有被其他接口调用  

