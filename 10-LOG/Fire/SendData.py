#!/usr/bin/python
# -*-coding:utf8-*-

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from LOG.Logger import Logger


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "argv error, SendData.py [ip] [count]"
        sys.exit(1)
    ip = sys.argv[1]
    cnt = int(sys.argv[2])
    logName = os.path.abspath("../logs/") + "/" + os.path.split(__file__)[1].split(".")[0] + ".log"
    logger = Logger.Logger(logName, os.path.split(__file__)[1]).getlog()
    configFile = "./config/data.config"
    # 1、发送测试数据:
    logger.info("发送数据中...")
    SendDataToKafka180(logName,logger).sendDataToKafka(configFile,ip,cnt)
    logger.info("发送数据结束")