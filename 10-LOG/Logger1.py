#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2019-12-29 04:04:25
@lastTime: 2020-05-17 01:57:07
@FilePath: \Turing\LOG\Logger1.py
@Description:
@version: 
'''


# -*- coding: utf-8 -*-

import logging


def logger(logger,logname,loglevel):
    # 创建一个logger
    logger = logging.getLogger(logger)
    logger.setLevel(logging.INFO)

    # 创建一个handler，用于写入日志文件
    fh = logging.FileHandler(logname)
    fh.setLevel(logging.INFO)

    # 再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # 定义handler的输出格式
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    format_dict = {
    1: logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
    2: logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
    3: logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
    4: logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
    5: logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    }
    formatter = format_dict[int(loglevel)]
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # 给logger添加handler
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logging


def testLogging():
    print(type(logging))
    logging.ERROR("error")


if __name__ == '__main__':
    mylog = logger("ceshi","test.log",1)
    mylog.warn("test")
    mylog.error("error")









