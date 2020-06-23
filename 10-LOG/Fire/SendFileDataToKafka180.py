#encoding: utf8
import pykafka
import json
import os
import time
import sys
import uuid
import base64
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from LOG.Logger import Logger


class SendFileDataToKafka():

    def __init__(self,logName):
        self.logName =logName
        self.logger = Logger(self.logName,os.path.split(__file__)[1]).getlog()

    def sendFileDataToKafka(self,configFile,kafkaIP,cnt):
        self.logger.warn('开始发送测试数据...')
        with open(configFile, 'r') as fp:
            for fileName in fp.readlines():
                fileName = fileName.strip()
                if not fileName.startswith('#'):
                    self.logger.warn("文件名为："+fileName)  # 需要记录的地方，用日志“标记”
                    with open(fileName, 'r') as f:
                        for line in f.readlines():
                            if not line.startswith('#'):
                                # self.logger.debug(line)
                                ## Setup kafka
                                client = pykafka.KafkaClient(hosts=kafkaIP+":9093")
                                topic = client.topics["ApiEvents"]
                                producer = topic.get_producer(compression=1, sync=True)
                                producer.start()
                                lineObj = self.encodeIsException(line)
                                if not lineObj :
                                    self.logger.warn("解码失败"+line)
                                    continue
                                lineObj["meta"]["tm"] = int(time.time())
                                # lineObj["net"]["dst_ip"] = "177.137.20.55"
                                # lineObj["net"]["dst_ip"] = "192.168.0.1"

                                for i in range(cnt):
                                    print lineObj
                                    lineObj['unique_id'] = {u"event_id": base64.b64encode(str(uuid.uuid5(uuid.NAMESPACE_DNS,str(uuid.uuid1()).replace("-", ""))).replace("-",""))}
                                    time.sleep(0.5)
                                    producer.produce(json.dumps(lineObj))
        self.logger.debug('Stopping Kafka producer')
        # print 'Stopping Kafka producer'
        producer.stop()
        self.logger.debug('停止kafka成功')
        # print '发送测试数据成功'
        self.logger.warn('测试数据发送成功！')
    def encodeIsException(self,line):
        codeList = ["UTF-8", "GBK", "GB2312", "ISO-8859-1", "LATIN1"]
        for code in codeList:
            # lineObj = self.isException(line, code)
            try:
                lineObj = json.loads(line, encoding=code)
            except ValueError as e:
                lineObj = None
            else:
                return lineObj
        return None



if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "argv error, SendFileDataKafka.py [ip] [count]"
        sys.exit(1)
    ip = sys.argv[1]
    cnt = int(sys.argv[2])
    logName = os.path.abspath("logs/").split("automatic-test")[0] + "automatic-test/logs/" + \
              os.path.split(__file__)[1].split(".")[0] + ".log"
    logger = Logger(logName, os.path.split(__file__)[1]).getlog()
    # configFile = u"./beta180config/doc-25K-wangpan.log"
    configFile = u"./beta180config/fileData.config"
    sendFileDataToKafka = SendFileDataToKafka(logName)
    sendFileDataToKafka.sendFileDataToKafka(configFile,ip,cnt)