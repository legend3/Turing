#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2019-12-22 11:35:22
@lastTime: 2020-05-19 03:39:00
@FilePath: \Turing\LOG\02.py
@Description: 
@version: 
'''


'''

1. 需求

现在有以下几个日志记录的需求：

    1）要求将所有级别的所有日志都写入磁盘文件中
    2）all.log文件中记录所有的日志信息，日志格式为：日期和时间 - 日志级别 - 日志信息
    3）error.log文件中单独记录error及以上级别的日志信息，日志格式为：日期和时间 - 日志级别 - 文件名[:行号] - 日志信息
    4）要求all.log在每天凌晨进行日志切割

2. 分析

    1）要记录所有级别的日志，因此日志器的有效level需要设置为最低级别--DEBUG;
    2）日志需要被发送到两个不同的目的地，因此需要为日志器设置两个handler；另外，两个目的地都是磁盘文件，因此这两个handler都是与FileHandler相关的；
    3）all.log要求按照时间进行日志切割，因此他需要用logging.handlers.TimedRotatingFileHandler; 而error.log没有要求日志切割，因此可以使用FileHandler;
    4）两个日志文件的格式不同，因此需要对这两个handler分别设置格式器；
'''

import logging
import logging.handlers
import datetime
import os


class ContextFilter(logging.Filter):
    """
    这是一个控制日志记录的过滤器。
    https://blog.csdn.net/Pythoncxy/article/details/96308952?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-6.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-6.nonecase
    """
    def filter(self, record):
        try:
            # lambda logLevel : logLevel.levelname <= logging.WARNING
            loggerName = record.name
            logMsg = record.msg
            logLevel = record.levelname
        except AttributeError:
            return False
        if loggerName == "mylogger" and logMsg == 'info message' or logLevel == 'WARNING':
            return True
        else:
            return False


# print(os.getcwd())
# 定义logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

# record = logging.LogRecord('mylogger')
'''
参数maxBytes和backupCount允许日志文件在达到maxBytes时rollover.当文件大小达到或者超过maxBytes时，就会新创建一个日志文件。
上述的这两个参数任一一个为0时，rollover都不会发生。也就是就文件没有maxBytes限制。
backupCount决定了能留几个日志文件。超过数量就会丢弃掉老的日志文件。

参数when决定了时间间隔的类型，参数interval决定了多少的时间间隔。如when=‘D’，interval=2，就是指两天的时间间隔
when的参数决定了时间间隔的类型。两者之间的关系如下：

'S'         |  秒

'M'         |  分

'H'         |  时

'D'         |  天

'W0'-'W6'   |  周一至周日

'midnight'  |  每天的凌晨

utc参数表示UTC时间
'''
# 为两个不同的文件设置不同的handler
rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight' , interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
rf_handler.addFilter(ContextFilter())  # addFilter方法需要一个filter对象，这里我定义一个新的类，并且重写filter方法,

f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

# 把相应的处理器组装到logger上
logger.addHandler(rf_handler)
logger.addHandler(f_handler)

# logger产生的日志(流线各个handler)
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
