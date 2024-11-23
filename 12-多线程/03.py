#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2019-12-22 11:35:22
lastTime: 2024-11-24 01:58:41
LastAuthor: Do not edit
FilePath: /Turing/12-多线程/03.py
Description: 
version: 
'''


#利用time延时函数,生成两个函数
# 利用多线程调用
# 计算总运行时间
# 练习带参数的多线程启动方法
import time
# 导入多线程包并更名为thread
import _thread as thread

def loop1(in1):
    # ctime 得到当前时间
    print('Start loop 1 at :', time.ctime())
    # 把参数打印出来
    print("我是参数 ",in1)
    # 睡眠多长时间,单位是秒
    time.sleep(4)
    print('End loop 1 at:', time.ctime())

def loop2(in1, in2):
    # ctime 得到当前时间
    print('Start loop 2 at :', time.ctime())
    # 把参数in 和 in2打印出来,代表使用
    print("我是参数 " ,in1 , "和参数  ", in2)
    # 睡眠多长时间,单位是秒
    time.sleep(2)
    print('End loop 2 at:', time.ctime())


if __name__ == "__main__":#主程序
    print("Starting at:", time.ctime())
    # 启动多线程的意思是用多线程去执行某个函数
    # 启动多线程函数为start_new_thead
    # 参数两个,一个是需要运行的函数名,第二是函数的参数作为元祖使用,为空则使用空元祖
    # 注意：如果函数只有一个参数,需要参数后由一个逗号
    thread.start_new_thread(loop1,("王老大", ))

    thread.start_new_thread(loop2,("王大鹏", "王晓鹏"))

    print("All done at:", time.ctime())
    # 一定要有while语句
    # 因为启动多线程后本程序就作为主线程存在！
    # 如果主线程执行完毕,则子线程可能也需要终止（守护线程在主线程运行结束后,也会结束运行,而非守护线程不会结束。）——此案例线程还未有start开启
    while True: # 阻止主线程关闭
        time.sleep(10)


'''
    使用了 _thread 模块,这是 Python 的一个较低级的线程模块。相比 threading 模块,_thread 的线程管理功能较少,且不具备自动等待子线程完成的能力。
    正因为这一点,当主线程执行结束后,程序会直接退出,而不会等待子线程完成。
'''