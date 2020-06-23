#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import logging.handlers
import logging.config


class Logger():
    def __init__(self, logName,logger):
        """

        :param logname:
        :param loglevel:
        :param logger:
        """
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)  # 会产生什么级别日志
        # logging.config.fileConfig(logName)

        # 创建一个handler，用于写入日志文件
        # fh = logging.FileHandler(logName)
        # 判断日志handler存在就不创建，如果不存在就创建
        if not self.logger.handlers:
            # 创建一个按大小切分日志文件的Handler
            fh = logging.handlers.RotatingFileHandler(logName,mode='a', maxBytes=1024*1024, backupCount=10)
            fh.setLevel(logging.DEBUG)  # 会处理什么级别日志

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
            formatter = format_dict[1]
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            # 给logger添加handler
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

            # logging.ERROR("error test")
    # 测试验证的方法
    def getlog(self):
        return self.logger


# 产生一个error日志测试验证
if __name__ == '__main__':
    logger = Logger(logname='log.txt', loglevel=1, logger="fox").getlog()
    logger.error("testtest")
