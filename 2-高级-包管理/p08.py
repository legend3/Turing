#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2019-12-22 11:35:22
@lastTime: 2020-05-04 23:38:27
@FilePath: \Turing\2-高级-包管理\p08.py
@Description: 
@version: 
'''


'''
    导入包及包中模块
'''
import pkg01.p01  # （包和模块都会可以被执行）最先执行p01中的输出    "我是模块p01呀，你特么的叫我干毛"

pkg01.inInit()  # 后于模块的print输出

stu = pkg01.p01.Student()
stu.say()

pkg01.p01.sayHello()


2020-05-04 23:30:27.582 [x_tunnel][ERROR] bind to b'127.0.0.1':1080 fail:OSError(10013, '以一种访问权限不允许的方式做了 一个访问套接字的尝试。', None, 10013, None)

Exception in thread Thread-46:
Traceback (most recent call last):
  File "E:\ChromeGo\XX-Net\code\default\lib\noarch\simple_http_server.py", line 463, in add_listen
    sock.bind(addr)
OSError: [WinError 10013] 以一种访问权限不允许的方式做了一个访问套接字的尝试。

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\ChromeGo\XX-Net\python3.8.2\lib\threading.py", line 932, in _bootstrap_inner
    self.run()
  File "E:\ChromeGo\XX-Net\python3.8.2\lib\threading.py", line 870, in run
    self._target(*self._args, **self._kwargs)
  File "E:\ChromeGo\XX-Net\code\default\x_tunnel\local\__init__.py", line 14, in start
    client.main(args)
  File "E:\ChromeGo\XX-Net\code\default\x_tunnel\local\client.py", line 178, in main
    g.socks5_server = simple_http_server.HTTPServer(addresses, Socks5Server, logger=xlog)
  File "E:\ChromeGo\XX-Net\code\default\lib\noarch\simple_http_server.py", line 430, in __init__
    self.init_socket()
  File "E:\ChromeGo\XX-Net\code\default\lib\noarch\simple_http_server.py", line 448, in init_socket
    self.add_listen((ip, port))
  File "E:\ChromeGo\XX-Net\code\default\lib\noarch\simple_http_server.py", line 467, in add_listen
    raise Exception(err_string)
Exception: bind to b'127.0.0.1':1080 fail:OSError(10013, '以一种访问权限不允许的方式做了一个访问套接字的尝试。', None, 10013, None)