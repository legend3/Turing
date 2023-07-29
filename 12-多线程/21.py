from multiprocessing import Process
import os


def info(title):
    print(title)
    print('module name:', __name__)
    # 获取父亲进程的id
    print('parent process:', os.getppid())
    # 获取本身进程的id
    print('process id:', os.getpid())


def f(name):
    info('function f')
    print('hello', name)


# 21.py程序进程(父) -> 主进程(父) -> 子进程
if __name__ == '__main__':
    info('main line') # 1. info由主进程触发
    p = Process(target=f, args=('bob',)) # 主进程创建子进程
    p.start() # 子进程被启动
    p.join()
