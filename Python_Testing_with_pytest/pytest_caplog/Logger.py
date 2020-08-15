#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging, logging.handlers, logging.config
'''
@Author: LEGEND
@since: 2020-07-03 03:31:19
@lastTime: 2020-07-03 04:28:14
@LastAuthor: Do not edit
@FilePath: \Turing\Python_Testing_with_pytest\pytest_caplog\test\Logger.py
@Description: 
@version: 
'''

class Logger():
    def __init__(self):
        # 读取日志配置文件内容
        logging.config.fileConfig('E:/workspace/Turing/Python_Testing_with_pytest/pytest_caplog/logging.conf')
        # 创建一个日志器logger
        self.logger = logging.getLogger('mylog')
    
    def getlog(self):
        return self.logger


# 日志输出
if __name__ == '__main__':
    logger = Logger().getlog()
    

    logger.debug('debug message')
    # logger.info('info message')
    # logger.warn('warn message')
    # logger.error('error message')
    # logger.critical('critical message')
