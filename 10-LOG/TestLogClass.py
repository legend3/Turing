#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2019-12-29 04:04:25
@lastTime: 2020-05-17 02:00:20
@FilePath: \Turing\LOG\TestLogClass.py
@Description: 
@version: 
'''


#!/usr/bin/python
# -*-coding:utf-8 -*-
from LOG.Logger import Logger
import logging


class Test():
    logger = Logger(logname='log.txt').getlog()
    def test(self):
        self.logger.error("testError")


if __name__ == '__main__':
    Test = Test()
    Test.test()
