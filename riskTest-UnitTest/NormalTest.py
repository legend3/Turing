#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
import random
import re
import os
import sys
import json
import logging
import time
import numpy as np
import math
import urlparse
import thread
from pykafka import KafkaClient
from lib.common import *
from lib.HttpRequest import *
import datetime


def getCurrentFunctionName():
    return inspect.stack()[1][3]

    # end def



class NormalThread(threading.Thread):
    def __init__(self, hosts, users_set, dateList,apiList,hourList,apiConfig,apiData):
        try:
            threading.Thread.__init__(self)
            self.hosts = hosts
            self.users= users_set
            self.dateList = dateList
            self.apiConfig = apiConfig
            self.apiData = apiData
            self.hourList = hourList
            self.apiList = apiList
            client = KafkaClient(hosts=self.hosts)
            topic = client.topics["ApiEvents"]
            self.producer = topic.get_sync_producer()
            # end try
        except Exception, e:
            ERROR(str(e))

    # end def

    def writeFileLog(self, msg, module='', level='error'):
        filename = os.path.split(__file__)[1]
        if level == 'debug':
            logging.getLogger().debug('File:' + filename + ', ' + module + ': ' + msg)
        elif level == 'warning':
            logging.getLogger().warning('File:' + filename + ', ' + module + ': ' + msg)
        else:
            logging.getLogger().error('File:' + filename + ', ' + module + ': ' + msg)
            # end if

    # end def

    # 调试日志
    def debug(self, msg, funcName=''):
        module = "%s.%s" % (self.module, funcName)
        msg = "threadName: %s, %s" % (self.threadName, msg)
        self.writeFileLog(msg, module, 'debug')

    # end def

    # 错误日志
    def error(self, msg, funcName=''):
        module = "%s.%s" % (self.module, funcName)
        msg = "threadName: %s, %s" % (self.threadName, msg)
        self.writeFileLog(msg, module, 'error')

    # end def



    def time_s(self,RandomSampling,batch_clock,batch_long,power_b,riqi):
        """
            获取当天每次访问的时间戳，也确定了该用户当天该时段内在该接口下访问的次数分布
                :param RandomSampling: 不放回抽样函数，抽取在时间段内的分钟
                :param batch_clock:当天时间段
                :param batch_long:时间段内一共访问的分钟数
                :param power_b: 当天该客户该时间段的访问强度，但未考虑接口因素
                :param riqi：当天日期，用于生成10位时间戳


        """
        stamp_list=[]
        clock=batch_clock.split("$")
        clock_stamp=[]

        for e in clock:
            total_t=riqi+" "+e
            ee=int(time.mktime(time.strptime(total_t, '%Y-%m-%d %H:%M:%S')) * 1000)
            clock_stamp.append(ee)
        min_long=int((clock_stamp[1]-clock_stamp[0])/60000)

        min_pool=[i for i in xrange(1,min_long)]
        min_info=RandomSampling(min_pool,batch_long)

        for m in min_info:
            m_num=sam_simple_po(1,power_b-4,5,12,1)[0]+1
            for j in xrange(m_num):
                tem=random.uniform(0, 60)
                total_stamp=int((clock_stamp[0]+60000*m+tem*1000)/1000)
                stamp_list.append(total_stamp)
        return stamp_list

    # end def

    def choice_time_during(self,hour_list, time_puch=3):
        # 根据概率获取3个工作时间段，按频率降序排列
        hour_now_list = []
        a=hour_list
        while len(hour_now_list) < time_puch:
            s_p = random.uniform(0, 1)
            if s_p <= 0.35:
                hour_now_list.append(hour_list[0])
            elif s_p <= 0.65:
                hour_now_list.append(hour_list[1])
            elif s_p <= 0.82:
                hour_now_list.append(hour_list[2])
            elif s_p <= 0.92:
                hour_now_list.append(hour_list[3])
            elif s_p <= 0.97:
                hour_now_list.append(hour_list[4])
            else:
                hour_now_list.append(hour_list[5])
            hour_now_list = list(set(hour_now_list))
        return hour_now_list

    # end def


    def send(self, apiEventList):
        try:
            if apiEventList is None or len(apiEventList) < 1:
                return None
            # end if



            for row in apiEventList:
                msg = json.write(row)
                # print msg
                self.producer.produce(msg)
                # end for
        except Exception, e:
            ERROR(str(e))
            return None

    # end def


    aa={"meta": {
        "tm": 1535359800,
        "session": {},
        "c_name": {},
        "c_uid": {}
    },
        "req": {
            "body": {
                "validate": "login",
                "userId": "werw",
                "password": "admin123456"
            },
            "remote_addr": '123.56.85.247',
            "url": "http://172.16.11.39/1.json",
            "args": {},
            "header": {
                "accept-language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                "accept-encoding": "gzip, deflate",
                "content-type": "application/json",
                "connection": "keep-alive",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0",
                "host": "http://172.16.11.39/1.json",
                "referer": "http://172.16.11.39/1.json",
                "pragma": "no-cache",
                "cache-control": "no-cache",
                "cookie": "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "upgrade-insecure-requests": "1"
            },
            "args2": {},
            "method": "POST"
        },
        "rsp": {
            "status": 200,
            "header": {
                "content-length": "178",
                "powered-by-chinacache": "MISS from 010106l3g5",
                "expires": "Mon, 19 Mar 2018 12:49:05 GMT",
                "server": "nginx/1.8.1",
                "connection": "keep-alive",
                "cache-control": "max-age=1800",
                "date": "Mon, 19 Mar 2018 12:19:06 GMT",
                "content-type": "application/json"
            },
            "body": "{\"phone\":\"15105512330\"}",
            "gzip_flag": 0,
            "set_cookies_list": [
                "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=admin; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"]
        }}



    def run(self):
        try:
            random.seed(10)
            user = "werw"
            size = 0
            # while True:
            try:
                url="http://172.16.11.39/1.json"
                ip= '123.56.85.247'
                body= "{\"phone\":\"15105512330\"}"
                data = { "meta": {
                "tm": 1535359800,
                "session": {},
                "c_name": {},
                "c_uid": {}
            },
            "req": {
                "body": {
                    "validate": "login",
                    "userId": "werw",
                    "password": "admin123456"
                },
                "remote_addr": '123.56.85.247',
                "url": "http://172.16.11.39/1.json",
                "args": {},
                "header": {
                    "accept-language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                    "accept-encoding": "gzip, deflate",
                    "content-type": "application/json",
                    "connection": "keep-alive",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0",
                    "host": "http://172.16.11.39/1.json",
                    "referer": "http://172.16.11.39/1.json",
                    "pragma": "no-cache",
                    "cache-control": "no-cache",
                    "cookie": "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                    "upgrade-insecure-requests": "1"
                },
                "args2": {},
                "method": "POST"
            },
            "rsp": {
                "status": 200,
                "header": {
                    "content-length": "178",
                    "powered-by-chinacache": "MISS from 010106l3g5",
                    "expires": "Mon, 19 Mar 2018 12:49:05 GMT",
                    "server": "nginx/1.8.1",
                    "connection": "keep-alive",
                    "cache-control": "max-age=1800",
                    "date": "Mon, 19 Mar 2018 12:19:06 GMT",
                    "content-type": "application/json"
                },
                "body":"{\"phone\":\"15105512330\"}",
                "gzip_flag": 0,
                "set_cookies_list": ["JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=admin; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" ]
            } }

                outs=[data,data]
                for each in outs:
                     self.send(each)
                     print "END"
                                                    # # print type(a)
                                                # # info=json.dumps(a)
                                                # info = json.write(a)

                                # #                 # producer.produce(info)
                                # print aaa


                    # except Exception, ge:
                    #     logging.error(ge)
                        # break
                    # end try

                    # self.debug("start to run user: %s, %d users wait to run" % (user, size))



            except Exception, e1:

                    # logging.error(e1)
                    self.error(str(e1), getCurrentFunctionName())
                    # self.error("run user: %s, Exception: %s" % (user, str(e1)))
                    # end try
                    # end while
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            # self.error(str(e))
            # end try
            # end def


# end class

def initApiData(api_seq,label_seq):
    """

    """
    try:
            a1 = "http://www.cdplatform.com/login.do"
            a2 = "http://www.cdplatform.com/bss/ncrm/ncustomer/nPanorama/profiling/json/datas.sdo"
            a3 = "http://www.cdplatform.com/bss/ncrm/ncustomer/customerListTable/json/getCustomerListData.sdo"
            a4 = "http://www.cdplatform.com/bss/ncrm/ncustomer/shop/abroad/html/datas.sdo"

            if api_seq == 2:
                phone = str(1396123) + str(label_seq + 1)
                email = "1536501%d@163.com" % (label_seq)
                card = "622700247017028%d" % (label_seq)
                pid = "32048119900410%d" % (label_seq)
                body = {"success": True, "data": {"user": "晓红", "phone": phone, "email": email, "card": card, "pid": pid}}
                info={"url":a2, "body": body}

            elif api_seq == 3:
                ddd = []
                for i in xrange(25):
                    seqq = (1813 * i) % 1000 + 10000 + label_seq
                    phone = str(139612) + str(seqq + 1)
                    email = "153652%d@qq.com" % (seqq)
                    card = "62270024701702%d" % (seqq)
                    pid = "3204811991041%d" % (seqq)
                    dd = {"user": "晓红", "phone": phone, "email": email, "card": card, "pid": pid}
                    ddd.append(dd)
                body = {"success": True, "data": ddd}
                info = {"url": a3, "body": body}


            elif api_seq ==4:
                detailBody = "<!DOCTYPE html>\n<html >\n  <head>\n    <meta charset=\"utf-8\">\n    <title> ShowDoc</title>\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <meta name=\"description\" content=\"\">\n    <meta name=\"author\" content=\"\">\n    <link href=\"/Public/bootstrap/css/bootstrap.min.css\" rel=\"stylesheet\">\n    <link href=\"/Public/css/showdoc.css\" rel=\"stylesheet\">\n      <script type=\"text/javascript\">\n      var DocConfig = {\n          host: window.location.origin,\n          app: \"/index.php?s=/\",\n          server: \"server/index.php?s=\",\n          pubile:\"/Public\",\n      }\n\n      DocConfig.hostUrl = DocConfig.host + \"/\" + DocConfig.app;\n      </script>\n      <script src=\"/Public/js/lang.zh-cn.js?v=212\"></script>\n  </head>\n  <body>\n\n<link rel=\"stylesheet\" href=\"/Public/css/item/index.css?v=1.234\" />\n    <div class=\"container-narrow\">\n\n      <div class=\"masthead\">\n        <div class=\"btn-group pull-right\">\n        <a class=\"btn btn-link\" href=\"https://github.com/star7th/showdoc/issues\" target=\"_blank\">反馈</a>\n        <a class=\"btn btn-link dropdown-toggle\" data-toggle=\"dropdown\" href=\"#\">\n       海外购物        <span class=\"caret\"></span>\n        </a>\n        <ul class=\"dropdown-menu\">\n        <!-- dropdown menu links -->\n          <li><a href=\"/index.php?s=/Home/User/setting\">个人设置</a></li>\n<!--           <li><a href=\"#share-home-modal\"  data-toggle=\"modal\">分享主页</a></li>\n -->      \n          <li><a href=\"/index.php?s=/Home/index/index\">网站首页</a></li>\n          <li><a href=\"/index.php?s=/Home/User/exist\">"
                detailBody += "email:%d@qq.com</a></li>\n\n        </ul>\n        </div>\n\n        </ul>\n        <h3 class=\"muted\"><img src=\"/Public/logo/b_64.png\" style=\"width:50px;height:50px;margin-bottom:15px;\" alt=\"\">ShowDoc</h3>\n      </div>\n\n      <hr>\n\n    <div class=\"container-thumbnails\">\n      <ul class=\"thumbnails\" id=\"item-list\">\n\n      </ul>\n    </div>\n\n\n    </div> <!-- /container -->\n\n<!-- 分享项目框 -->\n<div class=\"modal hide fade\" id=\"share-home-modal\">\n  <div class=\"modal-header\">\n    <button type=\"button\" class=\"close\" data-dismiss=\"modal\" aria-hidden=\"true\">&times;</button>\n  </div>\n  <div class=\"modal-body\">\n    <p>" % (
                    1396123 + label_seq)

                detailBody += "Card:622700247017027%d,Passport:E%d,ID:320111199511210414</p>\n  </div>\n</div>\n\n\n    \n\t<script src=\"/Public/js/beta131common/jquery.min.js\"></script>\n    <script src=\"/Public/bootstrap/js/bootstrap.min.js\"></script>\n    <script src=\"/Public/js/beta131common/showdoc.js?v=1.1\"></script>\n    <script src=\"/Public/layer/layer.js\"></script>\n    <script src=\"/Public/js/dialog.js\"></script>\n    <div style=\"display:none\">\n    \t    </div>\n  </body>\n</html> \n\n <script src=\"/Public/js/item/index.js?v=12\"></script>" % (
                    23 + label_seq, 87555321 + label_seq)
                body = detailBody
                info = {"url": a4, "body": body}


            elif api_seq ==1:
                info={"url": a1, "body": {}}

            return info
    except Exception, e:
        ERROR(str(e))
        return None
        # end try


# end def


def initIpList():
    try:
        data_inner=["192.168.9."+str(i) for i in xrange(5,200)]
        data_add = ['84.235.122.205', '75.193.225', '75.193.251', '202.100.073.255', '202.101.104.031', '202.101.096.127',
         '202.100.193.255', '202.100.096.252', '62.164.192.61', '202.99.197.255', '202.98.255.255', '202.98.202.255',
         '202.098.166.255', '202.098.107.253', '202.098.032.255', '202.098.022.255', '202.97.225.255', '56.23.52.31',
         ' 202.096.141.255', '202.096.136.255', '202.96.107.255', '62.164.192.63', '56.23.52.21', '218.244.140.225',
         '121.4.0.87', '121.194.0.93', '117.72.0.81', '125.118.250.127', '122.67.142.96', '121.47.0.89', '116.231.152.39',
         '182.92.242.11', '122.9.47.94', '125.119.9.31',"169.235.24.133","62.164.192.64",'121.100.161.92', '125.119.10.87', '121.40.68.88', '125.119.1.207',
         '125.119.3.7', '58.24.0.1', '111.1.36.6', '125.119.4.63', '125.118.251.183', '122.49.0.95', '122.70.9.97',
         '123.56.85.247', '84.235.122.215', '125.118.252.239', '118.144.0.85', '121.51.126.90', '125.118.249.71',
         '125.118.255.95', '117.53.48.80', '124.74.129.54', '116.242.0.79', '122.102.0.98', '117.103.128.82', '114.80.143.142',
         '221.130.202.206', '125.119.0.151', '116.228.3.82', '111.155.116.211', '125.119.6.175', '125.119.6.175',
         '218.244.140.225', '121.4.0.87', '121.194.0.93', '117.72.0.81', '125.118.250.127', '122.67.142.96', '121.47.0.89',
         '116.231.152.39', '182.92.242.11', '122.9.47.94', '125.119.9.31', '121.100.161.92', '125.119.10.87', '121.40.68.88',
         '125.119.1.207', '125.119.3.7', '58.24.0.1', '111.1.36.6', '125.119.4.63', '125.118.251.183', '122.49.0.95',
         '122.70.9.97', '56.23.52.42', '117.106.0.83', '125.118.252.239', '118.144.0.85', '121.51.126.90', '125.118.249.71',
         '125.118.255.95', '117.53.48.80', '124.74.129.54', '116.242.0.79', '122.102.0.98', '56.23.52.11', '114.80.143.142',
         '221.130.202.206', '125.119.0.151', '116.228.3.82', '111.155.116.211']
        data =list(set(data_inner+data_add))


        return data
    except Exception, e:
        ERROR(str(e))
        return None
        # end try


# end def

def initApiConfig(url,tm,ip,user,body):
    try:
        data = {
            "meta": {
                "tm": tm,
                "session": {},
                "c_name": {},
                "c_uid": {}
            },
            "req": {
                "body": {
                    "validate": "login",
                    "userId": user,
                    "password": "admin123456"
                },
                "remote_addr": ip,
                "url": url,
                "args": {},
                "header": {
                    "accept-language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                    "accept-encoding": "gzip, deflate",
                    "content-type": "application/json",
                    "connection": "keep-alive",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0",
                    "host": url,
                    "referer": url,
                    "pragma": "no-cache",
                    "cache-control": "no-cache",
                    "cookie": "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                    "upgrade-insecure-requests": "1"
                },
                "args2": {},
                "method": "POST"
            },
            "rsp": {
                "status": 200,
                "header": {
                    "content-length": "178",
                    "powered-by-chinacache": "MISS from 010106l3g5",
                    "expires": "Mon, 19 Mar 2018 12:49:05 GMT",
                    "server": "nginx/1.8.1",
                    "connection": "keep-alive",
                    "cache-control": "max-age=1800",
                    "date": "Mon, 19 Mar 2018 12:19:06 GMT",
                    "content-type": "application/json"
                },
                "body": body,
                "gzip_flag": 0,
                "set_cookies_list": ["JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=admin; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" ]
            }
        }

        return data
    except Exception, e:
        ERROR(str(e))
        return None
        # end try


# end def

def initUserList(count):
    try:
        data =['htoedi', 'ayvzyf', 'hvixhx', 'gotbiq', 'ukeqqx', 'hwvuat', 'ewlwrt', 'xxjxzo', 'uibixg', 'qlgwas', 'gbrpfa', 'qgplcx', 'rjvodk', 'siipeo', 'myquzl', 'thwyrq', 'towlik', 'unqzdk', 'qtmvpm', 'zmefsx', 'nhvtmg', 'ztqysq', 'kucgtz', 'regsbx', 'ugfqok', 'cyefuc', 'pagirc', 'xmdupy', 'urhzfi', 'odyzcj', 'youvbt', 'mdllxc', 'bdpppl', 'jxzcdg', 'cdulmn', 'seyvbv', 'ufcvmw', 'ujrsav', 'niqxos', 'excgsh', 'yyvxck', 'xkqlwe', 'uffmip', 'zkinmv', 'dpirju', 'tlchtn', 'wfxipx', 'zzszvy', 'oktgtn', 'qcueut', 'hufzma', 'cqtuco', 'qjaqno', 'qvtqoh', 'ikdqux', 'uocryb', 'qmnaah', 'xvghdc', 'onllzl', 'uuahir', 'rdadkg', 'gwfakc', 'qxdaoh', 'acvtyg', 'hyjksl', 'zbryvu', 'zletbq', 'noowmw', 'wfcbgk', 'wegyle', 'timhgl', 'nozfke', 'lueglj', 'khvcku', 'vzcqhf', 'uptsox', 'vgufoq', 'jevmqt', 'tevmar', 'geggsb', 'lfpbqi', 'wsfluz', 'nkcdoh', 'lqqbiu', 'qztxal', 'fymzqv', 'blpsix', 'pciwpv', 'kfypnp', 'vgsyvt', 'stmzzg', 'teocti', 'jrmhzi', 'jmgtlx', 'hrxbct', 'onfywk', 'pjodll', 'vmpnjg', 'vifihu', 'bjmuan', 'xqvdcx', 'zwucdz', 'lwvluv', 'ypkehk', 'ecwiit', 'kmlzue', 'pxgatz', 'fmvwnd', 'fdahgf', 'zmwpdj', 'wfhkbf', 'tboxpy', 'fcitcu', 'oiswkn', 'mxjmmf', 'mbdalb', 'zgealm', 'paavjt', 'oxezvc', 'vbpuox', 'qsuklu', 'fgiicg', 'ebikiw', 'stftgq', 'hvsjwm', 'loogpz', 'dpdlyz', 'fdjpxv', 'bpebjp', 'msomwz', 'fbftcv', 'jdahqu', 'ggbjlw', 'ypiugj']
        if count<len(data):
            return data[:count+1]
        else:
            return data
    except Exception, e:
        ERROR(str(e))
        return None
        # end try


# end def


def initHourList():
    try:
        data=["09:00:00$12:00:00","15:00:00$18:00:00","13:00:00$15:00:00","19:00:00$20:00:00","20:00:00$21:00:00","21:00:00$23:00:00"]

        return data
    except Exception, e:
        ERROR(str(e))
        return None
        # end try


# end def




def initDateList(date_str,date_length):
    """
       获取造数据的日期列表，得到日期和星期
       :param date_str: 数据的事件的起始日期，时间格式'%Y-%m-%d'
       :param date_length:持续天数

    """
    try:

        date_list = []
        dt = date_str
        dt_line = datetime.datetime(int(dt[0:4]), int(dt[5:7]), int(dt[8:10]))
        for i in xrange(date_length):
            date_elem = {}
            t = dt_line + datetime.timedelta(days=i)
            riqi = t.strftime('%Y-%m-%d')
            anyday = datetime.datetime(int(riqi[0:4]), int(riqi[5:7]), int(riqi[8:10])).strftime("%w");
            date_elem["riqi"] = riqi
            date_elem["xinqi"] = anyday
            date_list.append(date_elem)
        return date_list
    except Exception, e:
        ERROR(str(e))
        return None
        # end try




def main_norml(hosts,threadNum,start_day,len_pan):
    try:
        userList = initUserList(120)
        dateList = initDateList(start_day,len_pan)
        apiconfig = initApiConfig
        hourList = initHourList()
        apiList=[1,2,3,4]
        apiData = initApiData
        ipList = initIpList()



        ii=0

        users_info=[]
        for user in userList:
            user=user
            ii+=1
            ip=ipList[ii+8]
            user_info = user+"$$"+ip
            users_info.append(user_info)

        users_set = list_of_groups(users_info, threadNum)

        # end for

        thread_list = []
        for i in range(threadNum):
            # broker,
            thread_list.append(NormalThread(hosts,users_set[i], dateList, apiList,hourList,apiconfig,apiData))
        #end for
        for t in thread_list:
            t.start()
        # end for
        for t in thread_list:
            t.join()
        # # end for
        #
        # print "success"

    except Exception, e:
        ERROR(str(e))
        # end try


# end def

if __name__ == '__main__':
    initLog(logging.DEBUG, logging.DEBUG, "logs/" + os.path.split(__file__)[1].split(".")[0] + ".log")

    # if len(sys.argv) != 3:
    #     print "argv error, Normal.py ip:port threadNum"
    #     sys.exit(1)
    # end if

    broker = "192.168.0.95:9093"
    threadNum = 1
    # threadNum=10
    start_day = "2018-08-27"
    len_pan = 8
    main_norml(broker, threadNum,start_day,len_pan)
    # main(threadNum)
# end if

