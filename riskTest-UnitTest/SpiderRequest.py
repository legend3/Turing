#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import os
import sys
import json
import logging
import time
import urlparse
import httplib2
#from pykafka import KafkaClient
from lib.common import *
from lib.HttpRequest import *

class Spider(threading.Thread):
    def __init__(self, threadName, hosts, cookie, tm):
        try:
            self.module = self.__class__.__name__
            threading.Thread.__init__(self)
            self.threadName = threadName
            self.hosts = hosts
            self.cookie = cookie
            self.tm = tm
            self.loginUrl = "http://10.2.30.161:8080/login.do"
            self.http = HttpRequest({"timeout":30, "cookie": self.cookie})

        except Exception,e:
            self.error(str(e), getCurrentFunctionName())
        #end try
    #end def

    def writeFileLog(self, msg, module = '', level = 'error'):
        filename = os.path.split(__file__)[1]
        if level == 'debug':
            logging.getLogger().debug('File:' + filename + ', ' + module + ': ' + msg)
        elif level == 'warning':
            logging.getLogger().warning('File:' + filename + ', ' + module + ': ' + msg)
        else:
            logging.getLogger().error('File:' + filename + ', ' + module + ': ' + msg)
        #end if
    #end def

    #调试日志
    def debug(self, msg, funcName = ''):
        module = "%s.%s" % (self.module, funcName)
        msg = "threadName: %s, %s" % (self.threadName, msg)
        self.writeFileLog(msg, module, 'debug')
    #end def

    #错误日志
    def error(self, msg, funcName = ''):
        module = "%s.%s" % (self.module, funcName)
        msg = "threadName: %s, %s" % (self.threadName, msg)
        self.writeFileLog(msg, module, 'error')
    #end def

    def getApiEventTemplate(self, params):
        try:
            tm = params.get("tm", int(time.time()))
            ip = params.get("ip", "127.0.0.1")
            url = params.get("url", "http://www.test.com/test.html")
            urlTuple = urlparse.urlparse(url)
            host = "unknown"
            if len(urlTuple) > 1:
                host = urlTuple[1]
            #end if
            method = params.get("method", "GET")
            getParams = params.get("getParams", {})
            postParams = params.get("postParams", {})
            cookie = params.get("cookie", "")
            ua = params.get("ua", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0")
            referer = params.get("referer", "http://%s/" % (host))
            body = params.get("body", "{}")
            bodyLen = len(body)
            setCookie = params.get("setCookie", "")

            obj = {
                "meta": {
                    "tm": tm,
                    "session": {},
                    "c_name": {},
                    "c_uid": {}
                },
                "req": {
                    "body": postParams,
                    "remote_addr": ip,
                    "url": url,
                    "args": getParams,
                    "header": {
                        "content-type":"application/json",
                        "accept-language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                        "accept-encoding": "gzip, deflate",
                        "connection": "keep-alive",
                        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                        "user-agent": ua,
                        "host": host,
                        "referer": referer,
                        "pragma": "no-cache",
                        "cache-control": "no-cache",
                        "cookie": cookie,
                        "upgrade-insecure-requests": "1"
                    },
                    "args2": {},
                    "method": method
                },
                "rsp": {
                    "status": 200,
                    "header": {
                        "content-length": bodyLen,
                        "powered-by-chinacache": "MISS from 010106l3g5",
                        "expires": "Mon, 19 Mar 2018 12:49:05 GMT",
                        "server": "nginx/1.8.1",
                        "connection": "keep-alive",
                        "cache-control": "max-age=1800",
                        "date": "Mon, 19 Mar 2018 12:19:06 GMT",
                        "content-type": "text/html"
                    },
                    "body": body,
                    "gzip_flag": 0,
                    "set_cookies_list": [setCookie]
                }
            }

            return obj
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return {}
        #end try
    #end def

    def requestAction(self, requestParams):
        try:
            url = requestParams["url"]
            method = requestParams["method"]
            params = requestParams["params"]
            headers = requestParams["headers"]

            res, content = self.http.request(url, method, params, headers)
            #res, content = (None, None)

            data = {
                "requestParams": requestParams,
                "res": str(res),
                "content": content
            }

            self.debug(json.write(data), getCurrentFunctionName())
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
        #end try  
    #end def

    def getApiConfig(self, action):
        try:
            data = {
                "login": {
                    "tm": 1533085200,
                    "ip": "192.168.0.100",
                    "url": "http://10.2.30.161:8080/login.do",
                    "getParams": {},
                    "postParams": {
                        "validate": "login",
                        "userId": "admin",
                        "password": "admin123456"
                    },
                    "method": "POST",
                    "cookie": "",
                    "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0",
                    "referer": "http://10.2.30.161:8080/",
                    "body": "{}",
                    "setCookie": ""
                },
                "allCustomer": {
                    "tm": 1533085200,
                    "ip": "192.168.0.100",
                    "url": "http://10.2.30.161:8080/bss/ncrm/ncustomer/customerListTable/json/getCustomerListData.sdo",
                    "getParams": {},
                    "postParams": {
                        "dataFlag": 2,
                        "pageSize": 30,
                        "isAdvence": "true",
                        "queryType": 1,
                        "customerType": 1,
                        "i_cxfs": 1,
                        "i_cxcj": 1,
                        "limitType": "",
                        "orgId": 860,
                        "sfczdkh": 0,
                        "i_khq": "",
                        "i_khbq": "",
                        "i_khgs": 1,
                        "pageNo": 1,
                        "i_customerKeyword": "",
                        "assetStart": "",
                        "assetEnd": "",
                        "paging": "true",
                        "count": -1
                    },
                    "method": "POST",
                    "cookie": "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=admin; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                    "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0",
                    "referer": "http://10.2.30.161:8080/",
                    "body": "{}",
                    "setCookie": ""
                },
                "customerDetail": {
                    "tm": 1533085200,
                    "ip": "192.168.0.100",
                    "url": "http://10.2.30.161:8080/bss/ncrm/ncustomer/nPanorama/profiling/json/datas.sdo",
                    "getParams": {},
                    "postParams": {
                        "$module": "basicInfo",
                        "queryKey": "customerCode||$uid",
                        "customerCode": 1118055
                    },
                    "method": "POST",
                    "cookie": "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=admin; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                    "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0",
                    "referer": "http://10.2.30.161:8080/bss/ncrm/ncustomer/customerListTable/json/getCustomerListData.sdo",
                    "body": "{}",
                    "setCookie": ""
                }
            }

            return data.get(action, {})
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return {}
        #end try
    #end def

    def runLoginCrashPwdKafka(self, tm, ip, user):
        try:
            loginParams = self.getApiConfig("login")

            apiEventList = []
            
            for i in range(200):
                tm += 1
                loginParams["tm"] = tm
                loginParams["ip"] = ip
                loginParams["postParams"] = {
                    "validate": "login",
                    "userId": user,
                    "password": "admin123456"
                }
                loginParams["setCookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID="+user+"; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                res = self.getApiEventTemplate(loginParams)
                apiEventList.append(res)
            #end for

            return apiEventList
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []
        #end try
    #end def

    def getLoginCookie(self):
        try:
            cookie = ""
            http = HttpRequest({"timeout": 30})
            method = "POST"
            params = {"validate": "login", "userId": self.username, "password": self.password}
            headers = {
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                "Connection": "keep-alive",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Host": "10.2.30.161:8080",
                "Origin": "http://10.2.30.161:8080",
                "Referer": "http://10.2.30.161:8080",
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
            }
            res, content = http.request(url, method, params, headers)
            if res.has_key("set-cookie"):
                cookie = res["set-cookie"]
            else:
                self.error("login failed，res: %s, content: %s" % (json.write(res), content), getCurrentFunctionName())
            #end if
            
            return cookie
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return ""
        #end try
    #end def

    def getCookieByUser(self, user):
        try:
            #JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=admin; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
            res = re.findall(r'UserID=(.+?);', self.cookie)
            if res is not None and len(res) > 0:
                oldUser = res[0]
                cookie = self.cookie.replace(oldUser, user)
                return cookie
            else:
                return self.cookie
            #end if
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return self.cookie
        #end try
    #end def

    def runLoginCrashPwd(self, user):
        try:
            loginData = {
                "url": "http://10.2.30.161:8080/login.do",
                "method": "POST",
                "params": {"validate": "login", "userId": user, "password": ""},
                "headers": {
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Host": "10.2.30.161:8080",
                    "Origin": "http://10.2.30.161:8080",
                    "Referer": "http://10.2.30.161:8080",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
                }
            }

            for i in range(50):
                loginData["params"]["password"] = "testtesttest-%d" % (i)
                self.requestAction(loginData)
                time.sleep(2)
            #end for

        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
        #end try
    #end def

    def runLogin(self, userList):
        try:
            loginData = {
                "url": "http://10.2.30.161:8080/login.do",
                "method": "POST",
                "params": {"validate": "login", "userId": "admin", "password": ""},
                "headers": {
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Host": "10.2.30.161:8080",
                    "Origin": "http://10.2.30.161:8080",
                    "Referer": "http://10.2.30.161:8080",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
                }
            }

            for user in userList:
                loginData["params"]["userId"] = user
                loginData["params"]["password"] = "testtesttest"
                self.requestAction(loginData)
            #end for

        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
        #end try
    #end def

    def runUa(self, user, ua):
        try:
            cookie = self.getCookieByUser(user)
            listData = {
                "url": "http://10.2.30.161:8080/bss/ncrm/ncustomer/customerListTable/json/getCustomerListData.sdo",
                "method": "POST",
                "params": {
                    "dataFlag": 2,
                    "pageSize": 30,
                    "isAdvence": "true",
                    "queryType": 1,
                    "customerType": 1,
                    "i_cxfs": 1,
                    "i_cxcj": 1,
                    "limitType": "",
                    "orgId": 860,
                    "sfczdkh": 0,
                    "i_khq": "",
                    "i_khbq": "",
                    "i_khgs": 1,
                    "pageNo": 1,
                    "i_customerKeyword": "",
                    "assetStart": "",
                    "assetEnd": "",
                    "paging": "true",
                    "count": -1
                },
                "headers": {
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Cookie": cookie,
                    "Host": "10.2.30.161:8080",
                    "Origin": "http://10.2.30.161:8080",
                    "Referer": "http://10.2.30.161:8080/bss/customer/page/index.sdo?queryType=1",
                    "User-Agent": ua,
                    "X-Requested-With": "XMLHttpRequest"
                }
            }
            detailData = {
                "url": "http://10.2.30.161:8080/bss/ncrm/ncustomer/nPanorama/profiling/json/datas.sdo",
                "method": "POST",
                "params": {
                    "$module": "basicInfo",
                    "queryKey": "customerCode||$uid",
                    "customerCode": 1118055
                },
                "headers": {
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Cookie": cookie,
                    "Host": "10.2.30.161:8080",
                    "Origin": "http://10.2.30.161:8080",
                    "Referer": "http://10.2.30.161:8080/bss/customer/page/index.sdo?queryType=1",
                    "User-Agent": ua,
                    "X-Requested-With": "XMLHttpRequest"
                }
            }

            for i in range(2):
                self.requestAction(listData)
                for k in range(30):
                    self.requestAction(detailData)
                    time.sleep(2)
                #end for
            #end for

        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
        #end try
    #end def

    def runReferer(self, user, referer):
        try:
            cookie = self.getCookieByUser(user)
            listData = {
                "url": "http://10.2.30.161:8080/bss/ncrm/ncustomer/customerListTable/json/getCustomerListData.sdo",
                "method": "POST",
                "params": {
                    "dataFlag": 2,
                    "pageSize": 30,
                    "isAdvence": "true",
                    "queryType": 1,
                    "customerType": 1,
                    "i_cxfs": 1,
                    "i_cxcj": 1,
                    "limitType": "",
                    "orgId": 860,
                    "sfczdkh": 0,
                    "i_khq": "",
                    "i_khbq": "",
                    "i_khgs": 1,
                    "pageNo": 1,
                    "i_customerKeyword": "",
                    "assetStart": "",
                    "assetEnd": "",
                    "paging": "true",
                    "count": -1
                },
                "headers": {
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Cookie": cookie,
                    "Host": "10.2.30.161:8080",
                    "Origin": "http://10.2.30.161:8080",
                    "Referer": referer,
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
                    "X-Requested-With": "XMLHttpRequest"
                }
            }
            detailData = {
                "url": "http://10.2.30.161:8080/bss/ncrm/ncustomer/nPanorama/profiling/json/datas.sdo",
                "method": "POST",
                "params": {
                    "$module": "basicInfo",
                    "queryKey": "customerCode||$uid",
                    "customerCode": 1118055
                },
                "headers": {
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Cookie": cookie,
                    "Host": "10.2.30.161:8080",
                    "Origin": "http://10.2.30.161:8080",
                    "Referer": referer,
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
                    "X-Requested-With": "XMLHttpRequest"
                }
            }

            for i in range(2):
                self.requestAction(listData)
                for k in range(30):
                    self.requestAction(detailData)
                    time.sleep(2)
                #end for
            #end for

        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
        #end try
    #end def

    def runNormal(self, user, loginCount, listCount, detailCount):
        try:
            cookie = self.getCookieByUser(user)

            loginData = {
                "url": "http://10.2.30.161:8080/login.do",
                "method": "POST",
                "params": {"validate": "login", "userId": user, "password": ""},
                "headers": {
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Host": "10.2.30.161:8080",
                    "Origin": "http://10.2.30.161:8080",
                    "Referer": "http://10.2.30.161:8080",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
                }
            }
            listData = {
                "url": "http://10.2.30.161:8080/bss/ncrm/ncustomer/customerListTable/json/getCustomerListData.sdo",
                "method": "POST",
                "params": {
                    "dataFlag": 2,
                    "pageSize": 30,
                    "isAdvence": "true",
                    "queryType": 1,
                    "customerType": 1,
                    "i_cxfs": 1,
                    "i_cxcj": 1,
                    "limitType": "",
                    "orgId": 860,
                    "sfczdkh": 0,
                    "i_khq": "",
                    "i_khbq": "",
                    "i_khgs": 1,
                    "pageNo": 1,
                    "i_customerKeyword": "",
                    "assetStart": "",
                    "assetEnd": "",
                    "paging": "true",
                    "count": -1
                },
                "headers": {
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Cookie": cookie,
                    "Host": "10.2.30.161:8080",
                    "Origin": "http://10.2.30.161:8080",
                    "Referer": "http://10.2.30.161:8080/bss/customer/page/index.sdo?queryType=1",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
                    "X-Requested-With": "XMLHttpRequest"
                }
            }
            detailData = {
                "url": "http://10.2.30.161:8080/bss/ncrm/ncustomer/nPanorama/profiling/json/datas.sdo",
                "method": "POST",
                "params": {
                    "$module": "basicInfo",
                    "queryKey": "customerCode||$uid",
                    "customerCode": 1118055
                },
                "headers": {
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Cookie": cookie,
                    "Host": "10.2.30.161:8080",
                    "Origin": "http://10.2.30.161:8080",
                    "Referer": "http://10.2.30.161:8080/bss/customer/page/index.sdo?queryType=1",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
                    "X-Requested-With": "XMLHttpRequest"
                }
            }

            # 登录
            for i in range(loginCount):
                self.requestAction(loginData)
                time.sleep(2)
            #end for

            # 查询列表和详情
            for j in range(listCount):
                self.requestAction(listData)
                for k in range(detailCount):
                    self.requestAction(detailData)
                    time.sleep(2)
                #end for
                time.sleep(2)
            #end for

        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
        #end try
    #end def

    def runAmountFreOverNormal(self, user, loginCount, listCount, detailCount):
        try:
            cookie = self.getCookieByUser(user)

            loginData = {
                "url": "http://10.2.30.161:8080/login.do",
                "method": "POST",
                "params": {"validate": "login", "userId": user, "password": ""},
                "headers": {
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Host": "10.2.30.161:8080",
                    "Origin": "http://10.2.30.161:8080",
                    "Referer": "http://10.2.30.161:8080",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
                }
            }
            listData = {
                "url": "http://10.2.30.161:8080/bss/ncrm/ncustomer/customerListTable/json/getCustomerListData.sdo",
                "method": "POST",
                "params": {
                    "dataFlag": 2,
                    "pageSize": 30,
                    "isAdvence": "true",
                    "queryType": 1,
                    "customerType": 1,
                    "i_cxfs": 1,
                    "i_cxcj": 1,
                    "limitType": "",
                    "orgId": 860,
                    "sfczdkh": 0,
                    "i_khq": "",
                    "i_khbq": "",
                    "i_khgs": 1,
                    "pageNo": 1,
                    "i_customerKeyword": "",
                    "assetStart": "",
                    "assetEnd": "",
                    "paging": "true",
                    "count": -1
                },
                "headers": {
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Cookie": cookie,
                    "Host": "10.2.30.161:8080",
                    "Origin": "http://10.2.30.161:8080",
                    "Referer": "http://10.2.30.161:8080/bss/customer/page/index.sdo?queryType=1",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
                    "X-Requested-With": "XMLHttpRequest"
                }
            }
            detailData = {
                "url": "http://10.2.30.161:8080/bss/ncrm/ncustomer/nPanorama/profiling/json/datas.sdo",
                "method": "POST",
                "params": {
                    "$module": "basicInfo",
                    "queryKey": "customerCode||$uid",
                    "customerCode": 1118055
                },
                "headers": {
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Cookie": cookie,
                    "Host": "10.2.30.161:8080",
                    "Origin": "http://10.2.30.161:8080",
                    "Referer": "http://10.2.30.161:8080/bss/customer/page/index.sdo?queryType=1",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
                    "X-Requested-With": "XMLHttpRequest"
                }
            }

            # 登录
            '''
            for i in range(loginCount):
                print "login request, ", i
                self.requestAction(loginData)
                time.sleep(30)
            #end for
            '''

            # 查询列表和详情
            for j in range(listCount):
                print "list request, ", j
                self.requestAction(listData)
                time.sleep(30)
            #end for

            for k in range(detailCount):
                print "detail request, ", k
                self.requestAction(detailData)
                time.sleep(30)
            #end for

        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
        #end try
    #end def

    def send(self, apiEventList):
        try:
            if apiEventList is None or len(apiEventList) < 1:
                return
            #end if

            client = KafkaClient(hosts = self.hosts)
            topic = client.topics["ApiEvents"]
            producer = topic.get_sync_producer()

            for row in apiEventList:
                msg = json.write(row)
                #print msg
                producer.produce(msg)
            #end for

        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
        #end try
    #end def

    def runCirclrAmount(self, tm, ip, user):
        try:
            listParams = self.getApiConfig("allCustomer")
            detailParams = self.getApiConfig("customerDetail")

            # 然后分页获取用户信息列表，然后获取用户详情
            apiEventList = []
            # 获取列表和获取详情
            for i in range(10):
                tm += 5
                listParams["tm"] = tm
                listParams["ip"] = ip
                listParams["cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID="+user+"; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                
                listBody = "{\"success\": true, \"data\":["
                for j in range(30):
                    listBody += "{\"user\": \"晓红\", \"phone\": \"%d\", \"email\": \"%d@163.com\", \"card\":\"6227002470170278192\", \"pid\": \"320481199004101010\"}," % (15365019832 + i + j, 15365019832 + i + j)
                #end for
                listBody = listBody[0:-1]
                listBody += "]}"

                listParams["body"] = listBody
                res = self.getApiEventTemplate(listParams)
                apiEventList.append(res)

                for k in range(300):
                    tm += 5
                    detailParams["tm"] = tm
                    detailParams["ip"] = ip
                    detailParams["cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID="+user+"; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                    
                    detailBody = "{\"success\": true, \"data\":"
                    detailBody += "{\"user\": \"晓红\", \"phone\": \"%d\", \"email\": \"%d@163.com\", \"card\":\"6227002470170278192\", \"pid\": \"320481199004101010\"}" % (15365019832 + i + k, 15365019832 + i + k)
                    detailBody += "}"

                    detailParams["body"] = detailBody

                    res = self.getApiEventTemplate(detailParams)
                    apiEventList.append(res)
                #end for
            #end for

            return apiEventList
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []
        #end try
    #end def

    def runCookieUseIps(self, tm, user, ipList):
        try:

            listParams = self.getApiConfig("allCustomer")
            detailParams = self.getApiConfig("customerDetail")

            apiEventList = []
            for ip in ipList:
                for i in range(5):
                    listParams["tm"] = tm
                    listParams["ip"] = ip
                    listParams["cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID="+user+"; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                    
                    listBody = "{\"success\": true, \"data\":["
                    for j in range(30):
                        listBody += "{\"user\": \"晓红\", \"phone\": \"%d\", \"email\": \"%d@163.com\", \"card\":\"6227002470170278192\", \"pid\": \"320481199004101010\"}," % (15365019832 + i + j, 15365019832 + i + j)
                    #end for
                    listBody = listBody[0:-1]
                    listBody += "]}"

                    listParams["body"] = listBody
                    res = self.getApiEventTemplate(listParams)
                    apiEventList.append(res)

                    for k in range(10):
                        detailParams["tm"] = tm
                        detailParams["ip"] = ip
                        detailParams["cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID="+user+"; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                        
                        detailBody = "{\"success\": true, \"data\":"
                        detailBody += "{\"user\": \"晓红\", \"phone\": \"%d\", \"email\": \"%d@163.com\", \"card\":\"6227002470170278192\", \"pid\": \"320481199004101010\"}" % (15365019832 + i + k, 15365019832 + i + k)
                        detailBody += "}"

                        detailParams["body"] = detailBody

                        res = self.getApiEventTemplate(detailParams)
                        apiEventList.append(res)
                    #end for
                #end for
            #end for

            return apiEventList
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []
        #end try
    #end def

    def runLabelCountPreOverNormal(self, tm, ip, user):
        try:
            listParams = self.getApiConfig("allCustomer")
            detailParams = self.getApiConfig("customerDetail")

            # 然后分页获取用户信息列表，然后获取用户详情
            apiEventList = []
            # 获取列表和获取详情
            for i in range(100):
                tm += 12
                listParams["tm"] = tm
                listParams["ip"] = ip
                listParams["cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID="+user+"; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                
                listBody = "{\"success\": true, \"data\":["
                for j in range(200):
                    listBody += "{\"user\": \"晓红\", \"phone\": \"%d\", \"email\": \"%d@163.com\", \"card\":\"6227002470170278192\", \"pid\": \"320481199004101010\"}," % (15365019832 + i + j, 15365019832 + i + j)
                #end for
                listBody = listBody[0:-1]
                listBody += "]}"

                listParams["body"] = listBody
                res = self.getApiEventTemplate(listParams)
                apiEventList.append(res)
            #end for

            return apiEventList
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []
        #end try
    #end def

    def runExceptTime(self, tm, user, ip):
        try:

            loginParams = self.getApiConfig("login")
            listParams = self.getApiConfig("allCustomer")
            detailParams = self.getApiConfig("customerDetail")

            # 自动登录，然后分页获取用户信息列表，然后获取用户详情
            apiEventList = []
            # 1、登录
            loginParams["tm"] = tm
            loginParams["ip"] = ip
            loginParams["postParams"] = {
                "validate": "login",
                "userId": user,
                "password": "admin123456"
            }
            loginParams["referer"] = ""
            loginParams["setCookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID="+user+"; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            res = self.getApiEventTemplate(loginParams)
            apiEventList.append(res)

            # 2、获取列表和获取详情
            for i in range(10):
                tm += 2
                listParams["tm"] = tm
                listParams["ip"] = ip
                listParams["referer"] = ""
                listParams["cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID="+user+"; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                res = self.getApiEventTemplate(listParams)
                apiEventList.append(res)

                for k in range(30):
                    tm += 2
                    detailParams["tm"] = tm
                    detailParams["ip"] = ip
                    detailParams["referer"] = ""
                    detailParams["cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID="+user+"; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                    res = self.getApiEventTemplate(detailParams)
                    apiEventList.append(res)
                #end for
            #end for

            return apiEventList
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []
        #end try
    #end def

    def run(self):
        try:
            if self.threadName == "normal":
                pass
            elif self.threadName == "runLoginCrashPwd":
                # 登录暴力破解
                self.runLoginCrashPwd("youvbt")
            elif self.threadName == "runLogin":
                # 刷库
                self.runLogin(['htoedi', 'ayvzyf', 'hvixhx', 'gotbiq', 'ukeqqx', 'hwvuat', 'ewlwrt', 'xxjxzo', 'uibixg', 'qlgwas', 'gbrpfa', 'qgplcx', 'rjvodk', 'siipeo', 'myquzl', 'thwyrq', 'towlik', 'unqzdk', 'qtmvpm', 'zmefsx', 'nhvtmg', 'ztqysq', 'kucgtz', 'regsbx', 'ugfqok', 'cyefuc', 'pagirc', 'xmdupy', 'urhzfi', 'odyzcj', 'youvbt', 'mdllxc', 'bdpppl', 'jxzcdg', 'cdulmn', 'seyvbv', 'ufcvmw', 'ujrsav', 'niqxos', 'excgsh', 'yyvxck', 'xkqlwe', 'uffmip', 'zkinmv', 'dpirju', 'tlchtn', 'wfxipx', 'zzszvy', 'oktgtn', 'qcueut', 'hufzma', 'cqtuco', 'qjaqno', 'qvtqoh', 'ikdqux', 'uocryb', 'qmnaah', 'xvghdc', 'onllzl', 'uuahir', 'rdadkg', 'gwfakc', 'qxdaoh', 'acvtyg', 'hyjksl', 'zbryvu', 'zletbq', 'noowmw', 'wfcbgk', 'wegyle', 'timhgl', 'nozfke', 'lueglj', 'khvcku', 'vzcqhf', 'uptsox', 'vgufoq', 'jevmqt', 'tevmar', 'geggsb', 'lfpbqi', 'wsfluz', 'nkcdoh', 'lqqbiu', 'qztxal', 'fymzqv', 'blpsix', 'pciwpv', 'kfypnp', 'vgsyvt', 'stmzzg', 'teocti', 'jrmhzi', 'jmgtlx', 'hrxbct', 'onfywk', 'pjodll', 'vmpnjg', 'vifihu', 'bjmuan', 'xqvdcx', 'zwucdz', 'lwvluv', 'ypkehk', 'ecwiit', 'kmlzue', 'pxgatz', 'fmvwnd', 'fdahgf', 'zmwpdj', 'wfhkbf', 'tboxpy', 'fcitcu', 'oiswkn', 'mxjmmf', 'mbdalb', 'zgealm', 'paavjt', 'oxezvc', 'vbpuox', 'qsuklu', 'fgiicg', 'ebikiw', 'stftgq', 'hvsjwm', 'loogpz', 'dpdlyz', 'fdjpxv', 'bpebjp', 'msomwz', 'fbftcv', 'jdahqu', 'ggbjlw', 'ypiugj'])
            elif self.threadName == "runUa":
                # UA异常
                self.runUa("htoedi", "Python-httplib2/2.7 (gzip)")
            elif self.threadName == "runReferer":
                # Referer异常
                self.runReferer("htoedi", "")
            elif self.threadName == "runIpOverUserCount":
                # IP上使用多个账号
                self.runNormal("qgplcx", 2, 5, 10)
                self.runNormal("rjvodk", 2, 5, 10)
                self.runNormal("siipeo", 2, 5, 10)
                self.runNormal("ypiugj", 2, 5, 10)
                self.runNormal("ggbjlw", 2, 5, 10)
                self.runNormal("jdahqu", 2, 5, 10)
                self.runNormal("fbftcv", 2, 5, 10)
                self.runNormal("siipeo", 2, 5, 10)
                self.runNormal("ebikiw", 2, 5, 10)
                self.runNormal("fgiicg", 2, 5, 10)
                self.runNormal("oxezvc", 2, 5, 10)
                self.runNormal("paavjt", 2, 5, 10)
                self.runNormal("zgealm", 2, 5, 10)
                self.runNormal("mbdalb", 2, 5, 10)
                self.runNormal("mxjmmf", 2, 5, 10)
                self.runNormal("oiswkn", 2, 5, 10)
                self.runNormal("fcitcu", 2, 5, 10)
            elif self.threadName == "dayAmountOverNormal":
                # 日访问次数偏移用户基线
                self.runAmountFreOverNormal("luobin", 30, 100, 300)
            elif self.threadName == "runAmountFreOverNormal":
                # 请求频次偏移基线
                self.runAmountFreOverNormal("tengwei", 2, 10, 300)
            elif self.threadName == "multiUserPreIp":
                # 单IP多账号
                pass
            elif self.threadName == "runCirclrAmount":
                # 周期性访问
                tm = self.tm + 3600 * 16 + 40 * 60
                apiEventList = self.runCirclrAmount(tm, "10.97.13.88", "bdpppl")
                self.send(apiEventList)
            elif self.threadName == "runCookieUseIps":
                # 同一个Cookie在不同的IP上使用
                tm = self.tm + 3600 * 18 + 600
                apiEventList = self.runCookieUseIps(tm, "myquzl", ["10.97.13.90", "10.97.13.91", "10.97.13.92"])
                self.send(apiEventList)
            elif self.threadName == "runLabelCountPreOverNormal":
                # 单次请求数据量偏离基线
                tm = self.tm + 3600 * 18 + 1200
                apiEventList = self.runLabelCountPreOverNormal(tm, "10.97.13.87", "thwyrq")
                self.send(apiEventList)
            elif self.threadName == "runExceptTime":
                # 异常时间段
                tm = self.tm + 3600 * 2 + 1200
                apiEventList = self.runExceptTime(tm, "gwfakc", "10.97.13.93")
                self.send(apiEventList)
            #end if

        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
        #end try
    #end def
#end class

def main(hosts, cookie):
    try:
        '''
        threadNameList = [
            "normal", 
            "runLoginCrashPwd", 
            "runLogin", 
            "runUa", 
            "runReferer", 
            "runIpOverUserCount", 
            "dayAmountOverNormal", 
            "runAmountFreOverNormal", 
            "runCirclrAmount",
        ]
        '''
        
        '''
        threadNameList = [
            "runCirclrAmount", 
            "runCookieUseIps",
            "runLabelCountPreOverNormal",
            "runExceptTime"
        ]
        '''

        threadNameList = [
            "dayAmountOverNormal"
        ]
        

        tm = formatToTime("2018-08-15 00:00:00")
        threadList = []
        for threadName in threadNameList:
            t = Spider(threadName, hosts, cookie, tm)
            threadList.append(t)
        #end for

        for t in threadList:
            t.start()
        #end for

        for t in threadList:
            t.join()
        #end for

    except Exception,e:
        print str(e)
    #end try
#end def

if __name__ == '__main__':
    initLog(logging.ERROR, logging.ERROR, "logs/" + os.path.split(__file__)[1].split(".")[0] + ".log")

    if len(sys.argv) != 4:
        print "argv error, SpiderRequest.py JSESSIONID UserID PortalToken"
        sys.exit(1)
    #end if

    hosts = "10.2.130.55:9093"
    #hosts = "192.168.0.96:9093"
    cookie = "JSESSIONID=%s; UserID=%s; PortalToken=%s" % (sys.argv[1], sys.argv[2], sys.argv[3])

    main(hosts, cookie)
#end if



