#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2019-12-22 11:35:22
@lastTime: 2020-05-18 02:33:50
@FilePath: \Turing\LOG\01.py
@Description: 
@version: 
'''


import logging

# 2.
"""
因为在logging模块提供的日志记录函数所使用的日志器设置的处理器所指定的日志输出位置默认为:
sys.stderr

怎么修改这些默认设置呢？
其实很简单，在我们调用上面这些日志记录函数之前，手动调用一下basicConfig()方法，把我们想设置的内容以参数的形式传递进去就可以了。

该函数可接收的关键字参数如下：

参数名称	描述
filename	指定日志输出目标文件的文件名，指定该设置项后日志信心就不会被输出到控制台了
filemode	指定日志文件的打开模式，默认为'a'。需要注意的是，该选项要在filename指定时才有效
format	指定日志格式字符串，即指定日志输出时所包含的字段信息以及它们的顺序。logging模块定义的格式字段下面会列出。
datefmt	指定日期/时间格式。需要注意的是，该选项要在format中包含时间字段%(asctime)s时才有效
level	指定日志器的日志级别
stream	指定日志输出目标stream，如sys.stdout、sys.stderr以及网络stream。需要说明的是，stream和filename不能同时提供，否则会引发 ValueError异常
style	Python 3.2中新添加的配置项。指定format格式字符串的风格，可取值为'%'、'{'和'$'，默认为'%'
handlers	Python 3.3中新添加的配置项。该选项如果被指定，它应该是一个创建了多个Handler的可迭代对象，这些handler将会被添加到root logger。需要说明的是：filename、stream和handlers这三个配置项只能有一个存在，不能同时出现2个或3个，否则会引发ValueError异常。
"""
LOG_FORMAT = "%(asctime)s-----%(levelname)s-----%(message)s"  # 日志格式
DATE_FORMAT = "%m/%d/%y-%H:%m:%s %p"  # 时间格式
logging.basicConfig(filename='LOG/turing.log', level=logging.DEBUG, format=LOG_FORMAT,datefmt=DATE_FORMAT)


# 1.(因为logging模块提供的日志记录函数所使用的日志器设置的日志级别是WARNING，
    # 因此只有WARNING级别的日志记录以及大于它的ERROR和CRITICAL级别的日志记录被输出了，
    # 而小于它的DEBUG和INFO级别的日志记录被丢弃了。)
logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")

# 另外一种写法
logging.log(logging.DEBUG, "This is a debug log.")
logging.log(logging.INFO, "This is a info log.")
logging.log(logging.WARNING, "This is a warning log.")
logging.log(logging.ERROR, "This is a error log.")
logging.log(logging.CRITICAL, "This is a critical log.")
