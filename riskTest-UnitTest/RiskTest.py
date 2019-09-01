#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import json
import logging
import time
import urlparse
from pykafka import KafkaClient
from lib.common import *
from lib.HttpRequest import *
from read_mongo import start_mongo_config
from create_normal_data import pre_data_main
from Normal import main_norml
import pymongo
from beta131.beta131common.ToolUtils import ToolUtils

from beta131.beta131common.MongoUtils import MongoUtils

reload(sys)
sys.setdefaultencoding('utf-8')


class Spider(threading.Thread):
    def __init__(self, threadName, hosts, tm):
        try:
            self.module = self.__class__.__name__
            threading.Thread.__init__(self)
            self.threadName = threadName
            self.hosts = hosts
            self.tm = tm

        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            # end try

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

    def getApiEventTemplate(self, params):
        try:
            tm = params.get("tm", int(time.time()))
            ip = params.get("ip", "127.0.0.1")
            url = params.get("url", "http://www.test.com/test.html")
            urlTuple = urlparse.urlparse(url)
            host = "unknown"
            if len(urlTuple) > 1:
                host = urlTuple[1]
            # end if
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
                        "content-type": "application/json",
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
            # end try

    # end def

    def requestAction(self, requestParams):
        try:
            url = requestParams["url"]
            method = requestParams["method"]
            params = requestParams["params"]
            headers = requestParams["headers"]

            res, content = self.http.request(url, method, params, headers)
            # res, content = (None, None)

            data = {
                "requestParams": requestParams,
                "res": res,
                "content": content
            }

            self.debug(json.write(data), getCurrentFunctionName())
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            # end try

    # end def

    def getApiConfig(self, action):
        try:
            data = {
                "login": {
                    "tm": 1533085200,
                    "ip": "192.168.0.100",
                    "url": "http://www.cdplatform.com/login.do",
                    "getParams": {},
                    "postParams": {
                        "validate": "login",
                        "userId": "admin",
                        "password": "admin123456"
                    },
                    "method": "POST",
                    "cookie": "",
                    "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0",
                    "referer": "http://www.cdplatform.com/",
                    "body": "{}",
                    "setCookie": ""
                },
                "allCustomer": {
                    "tm": 1533085200,
                    "ip": "192.168.0.100",
                    "url": "http://www.cdplatform.com/bss/ncrm/ncustomer/customerListTable/json/getCustomerListData.sdo",
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
                    "referer": "http://www.cdplatform.com/",
                    "body": "{}",
                    "setCookie": ""
                },
                "customerDetail": {
                    "tm": 1533085200,
                    "ip": "192.168.0.100",
                    "url": "http://www.cdplatform.com/bss/ncrm/ncustomer/nPanorama/profiling/json/datas.sdo",
                    "getParams": {},
                    "postParams": {
                        "$module": "basicInfo",
                        "queryKey": "customerCode||$uid",
                        "customerCode": 1118055
                    },
                    "method": "POST",
                    "cookie": "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=admin; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                    "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0",
                    "referer": "http://www.cdplatform.com/bss/ncrm/ncustomer/customerListTable/json/getCustomerListData.sdo",
                    "body": "{}",
                    "setCookie": ""
                },
                "shopAbroad": {
                    "tm": 1533085200,
                    "ip": "192.168.0.100",
                    "url": "http://www.cdplatform.com/bss/ncrm/ncustomer/shop/abroad/html/datas.sdo",
                    "getParams": {},
                    "postParams": {
                        "$module": "basicInfo",
                        "queryKey": "customerCode||$uid",
                        "customerCode": 1118055
                    },
                    "method": "POST",
                    "cookie": "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=admin; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                    "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0",
                    "referer": "http://www.cdplatform.com/bss/ncrm/ncustomer/customerListTable/json/getCustomerListData.sdo",
                    "body": "{}",
                    "setCookie": ""

                },
                "companyCustomer":
                    {
                        "tm": 1533085200,
                        "ip": "192.168.0.100",
                        "url": "http://www.cdplatform.com/bss/ncrm/company/xml/datas.sdo",
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
                        "referer": "http://www.cdplatform.com/",
                        "body": "{}",
                        "setCookie": ""
                    }
            }

            return data.get(action, {})
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return {}
            # end try

    # end def
    def get_api(self, api_list, tm, ip, ua, content, user, outer_circle, outer_later, content_length, inner_circle,
                inner_later, referer):
        try:
            apis_config = {}
            for api, api_value in api_list.items():
                apis_config[api] = {}
                if api_value:
                    api_config = self.getApiConfig(api)
                apis_config[api] = api_config

            # 然后分页获取用户信息列表，然后获取用户详情
            apiEventList = []
            # 获取列表和获取详情
            for i in range(outer_circle):
                allCustomer = apis_config["allCustomer"]
                if allCustomer:
                    listParams = allCustomer
                    tm += outer_later
                    listParams["tm"] = tm
                    listParams["ip"] = ip
                    if not referer:
                        listParams["referer"] = referer
                    if ua:
                        listParams["ua"] = ua
                    if content:
                        listParams[
                            "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

                        listBody = "{\"success\": true, \"data\":["
                        for j in range(content_length):
                            listBody += "{\"user\": \"晓红\", \"phone\": \"%d\", \"email\": \"%d@163.com\", \"card\":\"6227002470170278192\", \"pid\": \"320481197004101010\"}," % (
                                15315012832 + i + j, 18075012832 + i + j)
                        # end for
                        listBody = listBody[0:-1]
                        listBody += "]}"

                        listParams["body"] = listBody
                    res = self.getApiEventTemplate(listParams)
                    apiEventList.append(res)

                for k in range(inner_circle):
                    customerDetail = apis_config["customerDetail"]
                    shopAbroad = apis_config["shopAbroad"]
                    if customerDetail:
                        detailParams = customerDetail
                        tm += inner_later
                        detailParams["tm"] = tm
                        detailParams["ip"] = ip
                        if not referer:
                            detailParams["referer"] = referer
                        if ua:
                            detailParams["ua"] = ua
                        if content:
                            detailParams[
                                "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

                            detailBody = "{\"success\": true, \"data\":"
                            detailBody += "{\"user\": \"晓红\", \"phone\": \"%d\", \"email\": \"%d@153.com\", \"card\":\"6227002670170278192\", \"pid\": \"320481197004101010\"}" % (
                                13965213832 + i + k, 18365011832 + i + k)
                            detailBody += "}"

                            detailParams["body"] = detailBody

                        res = self.getApiEventTemplate(detailParams)
                        apiEventList.append(res)
                    if shopAbroad:
                        detailParams_a = shopAbroad
                        tm += inner_later / 2
                        detailParams_a["tm"] = tm
                        detailParams_a["ip"] = ip
                        if not referer:
                            detailParams["referer"] = referer
                        if ua:
                            detailParams_a["ua"] = ua
                        if content:
                            detailParams_a[
                                "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

                            detailBody = "<!DOCTYPE html>\n<html >\n  <head>\n    <meta charset=\"utf-8\">\n    <title> ShowDoc</title>\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <meta name=\"description\" content=\"\">\n    <meta name=\"author\" content=\"\">\n    <link href=\"/Public/bootstrap/css/bootstrap.min.css\" rel=\"stylesheet\">\n    <link href=\"/Public/css/showdoc.css\" rel=\"stylesheet\">\n      <script type=\"text/javascript\">\n      var DocConfig = {\n          host: window.location.origin,\n          app: \"/index.php?s=/\",\n          server: \"server/index.php?s=\",\n          pubile:\"/Public\",\n      }\n\n      DocConfig.hostUrl = DocConfig.host + \"/\" + DocConfig.app;\n      </script>\n      <script src=\"/Public/js/lang.zh-cn.js?v=212\"></script>\n  </head>\n  <body>\n\n<link rel=\"stylesheet\" href=\"/Public/css/item/index.css?v=1.234\" />\n    <div class=\"container-narrow\">\n\n      <div class=\"masthead\">\n        <div class=\"btn-group pull-right\">\n        <a class=\"btn btn-link\" href=\"https://github.com/star7th/showdoc/issues\" target=\"_blank\">反馈</a>\n        <a class=\"btn btn-link dropdown-toggle\" data-toggle=\"dropdown\" href=\"#\">\n       海外购物        <span class=\"caret\"></span>\n        </a>\n        <ul class=\"dropdown-menu\">\n        <!-- dropdown menu links -->\n          <li><a href=\"/index.php?s=/Home/User/setting\">个人设置</a></li>\n<!--           <li><a href=\"#share-home-modal\"  data-toggle=\"modal\">分享主页</a></li>\n -->      \n          <li><a href=\"/index.php?s=/Home/index/index\">网站首页</a></li>\n          <li><a href=\"/index.php?s=/Home/User/exist\">"
                            detailBody += "email:%d@qq.com</a></li>\n\n        </ul>\n        </div>\n\n        </ul>\n        <h3 class=\"muted\"><img src=\"/Public/logo/b_64.png\" style=\"width:50px;height:50px;margin-bottom:15px;\" alt=\"\">ShowDoc</h3>\n      </div>\n\n      <hr>\n\n    <div class=\"container-thumbnails\">\n      <ul class=\"thumbnails\" id=\"item-list\">\n\n      </ul>\n    </div>\n\n\n    </div> <!-- /container -->\n\n<!-- 分享项目框 -->\n<div class=\"modal hide fade\" id=\"share-home-modal\">\n  <div class=\"modal-header\">\n    <button type=\"button\" class=\"close\" data-dismiss=\"modal\" aria-hidden=\"true\">&times;</button>\n  </div>\n  <div class=\"modal-body\">\n    <p>" % (
                            15365419832 + i + k)

                            detailBody += "Card:6227001470170278192,Passport:E%d,ID:320111199111210414</p>\n  </div>\n</div>\n\n\n    \n\t<script src=\"/Public/js/beta131common/jquery.min.js\"></script>\n    <script src=\"/Public/bootstrap/js/bootstrap.min.js\"></script>\n    <script src=\"/Public/js/beta131common/showdoc.js?v=1.1\"></script>\n    <script src=\"/Public/layer/layer.js\"></script>\n    <script src=\"/Public/js/dialog.js\"></script>\n    <div style=\"display:none\">\n    \t    </div>\n  </body>\n</html> \n\n <script src=\"/Public/js/item/index.js?v=12\"></script>" % (
                            87555321 + i + k)

                            detailParams_a["body"] = detailBody

                        res = self.getApiEventTemplate(detailParams_a)
                        apiEventList.append(res)
            return apiEventList
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []


            # end for
            # end for

    def runNormal(self, tm, ip, user):
        try:
            tm = tm + 3600 * 9 + 600
            api_list = {"customerDetail": 1, "shopAbroad": 1, "allCustomer": 1}
            outer_circle = 20
            outer_later = 10
            inner_circle = 30
            inner_later = 60
            ua = 0
            content = 1
            content_length = 30
            referer = 1
            apiEventList = self.get_api(api_list, tm, ip, ua, content, user, outer_circle, outer_later, content_length,
                                        inner_circle, inner_later, referer)
            return apiEventList


        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []

    def runNormal_pre(self, tm, ip, user):
        try:
            tm = tm + 3600 * 9 + 600

            listParams = self.getApiConfig("allCustomer")
            detailParams = self.getApiConfig("customerDetail")

            # 然后分页获取用户信息列表，然后获取用户详情
            apiEventList = []
            # 获取列表和获取详情
            for i in range(20):
                tm += 10
                listParams["tm"] = tm
                listParams["ip"] = ip
                listParams[
                    "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

                listBody = "{\"success\": true, \"data\":["
                for j in range(30):
                    listBody += "{\"user\": \"晓红\", \"phone\": \"%d\", \"email\": \"%d@163.com\", \"card\":\"6227002470170278192\", \"pid\": \"320481199004101010\"}," % (
                    15365019832 + i + j, 15365019832 + i + j)
                # end for
                listBody = listBody[0:-1]
                listBody += "]}"

                listParams["body"] = listBody
                res = self.getApiEventTemplate(listParams)
                apiEventList.append(res)

                for k in range(30):
                    tm += 60
                    detailParams["tm"] = tm
                    detailParams["ip"] = ip
                    detailParams[
                        "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

                    detailBody = "{\"success\": true, \"data\":"
                    detailBody += "{\"user\": \"晓红\", \"phone\": \"%d\", \"email\": \"%d@163.com\", \"card\":\"6227002470170278192\", \"pid\": \"320481199004101010\"}" % (
                    15365019832 + i + k, 15365019832 + i + k)
                    detailBody += "}"

                    detailParams["body"] = detailBody

                    res = self.getApiEventTemplate(detailParams)
                    apiEventList.append(res)



                    # end for
            # end for

            return apiEventList
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []
            # end try

    # end def

    def runLoginCrashPwd(self, tm, ip, user):
        try:
            tm = tm + 3600 * 10 + 60

            loginParams = self.getApiConfig("login")

            apiEventList = []

            for i in range(50):
                tm += 1
                loginParams["tm"] = tm
                loginParams["ip"] = ip
                loginParams["postParams"] = {
                    "validate": "login",
                    "userId": user,
                    "password": "admin123456"
                }
                loginParams[
                    "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                res = self.getApiEventTemplate(loginParams)
                apiEventList.append(res)
            # end for

            return apiEventList
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []
            # end try

    # end def

    def runLogin(self, tm, ip, userList):
        try:
            tm = tm + 3600 * 10 + 60

            loginParams = self.getApiConfig("login")

            apiEventList = []

            for user in userList:
                tm += 1
                loginParams["tm"] = tm
                loginParams["ip"] = ip
                loginParams["postParams"] = {
                    "validate": "login",
                    "userId": user,
                    "password": "admin123456"
                }
                loginParams[
                    "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                res = self.getApiEventTemplate(loginParams)
                apiEventList.append(res)
            # end for

            return apiEventList
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []
            # end try

    # end def
    def runUa_currency(self, tm, ip, user, ua):
        try:
            tm = tm + 3600 * 10 + 1800
            api_list = {"customerDetail": 1, "shopAbroad": 1, "allCustomer": 1}
            outer_circle = 5
            outer_later = 1
            inner_circle = 10
            inner_later = 0.5
            content = 0
            content_length = 0
            referer = 1
            # 自动登录，然后分页获取用户信息列表，然后获取用户详情
            apiEventList = []
            # 1、登录
            loginParams = self.getApiConfig("login")
            loginParams["tm"] = tm
            loginParams["ip"] = ip
            loginParams["postParams"] = {
                "validate": "login",
                "userId": user,
                "password": "admin123456"
            }
            loginParams["ua"] = ua
            loginParams[
                "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            res = self.getApiEventTemplate(loginParams)
            apiEventList.append(res)
            # 2、获取列表和获取详情
            apiEventList = self.get_api(api_list, tm, ip, ua, content, user, outer_circle, outer_later, content_length,
                                        inner_circle, inner_later, referer)
            return apiEventList

        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []

    def runUa(self, tm, ip, user, ua):
        try:
            # tm = formatToTime("%s 10:30:00" % (date))
            tm = tm + 3600 * 10 + 1800

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
            loginParams["ua"] = ua
            loginParams[
                "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            res = self.getApiEventTemplate(loginParams)
            apiEventList.append(res)

            # 2、获取列表和获取详情
            for i in range(5):
                tm += 1
                listParams["tm"] = tm
                listParams["ip"] = ip
                listParams["ua"] = ua
                listParams[
                    "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                res = self.getApiEventTemplate(listParams)
                apiEventList.append(res)

                for k in range(10):
                    tm += 0.5
                    detailParams["tm"] = tm
                    detailParams["ip"] = ip
                    detailParams["ua"] = ua
                    detailParams[
                        "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                    res = self.getApiEventTemplate(detailParams)
                    apiEventList.append(res)
                    # end for
            # end for

            return apiEventList
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []
            # end try

    # end def
    def runDayAmountOverNormal_currency(self, tm, ip, user):
        try:
            # tm = formatToTime("%s 10:40:00" % (date))
            tm = tm + 3600 * 10 + 2400
            api_list = {"customerDetail": 1, "shopAbroad": 1, "allCustomer": 1}
            outer_circle = 200
            outer_later = 1
            inner_circle = 10
            inner_later = 5
            ua = ""
            content = 0
            content_length = 0
            referer = 1
            apiEventList = self.get_api(api_list, tm, ip, ua, content, user, outer_circle, outer_later, content_length,
                                        inner_circle,
                                        inner_later, referer)
            return apiEventList
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []

    def runDayAmountOverNormal(self, tm, ip, user):
        try:
            # tm = formatToTime("%s 10:40:00" % (date))
            tm = tm + 3600 * 10 + 2400

            listParams = self.getApiConfig("allCustomer")
            detailParams = self.getApiConfig("customerDetail")

            # 然后分页获取用户信息列表，然后获取用户详情
            apiEventList = []
            # 获取列表和获取详情
            for i in range(100):
                tm += 1
                listParams["tm"] = tm
                listParams["ip"] = ip
                listParams[
                    "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                res = self.getApiEventTemplate(listParams)
                apiEventList.append(res)

                for k in range(10):
                    tm += 5
                    detailParams["tm"] = tm
                    detailParams["ip"] = ip
                    detailParams[
                        "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                    res = self.getApiEventTemplate(detailParams)
                    apiEventList.append(res)
                    # end for
            # end for

            return apiEventList
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []
            # end try

    # end def
    def runDayAmountLargeOverNormal_currency(self, tm, ip, user):
        try:
            tm = tm + 3600 * 10 + 2400
            api_list = {"customerDetail": 1, "shopAbroad": 1, "allCustomer": 1}
            outer_circle = 310
            outer_later = 1
            inner_circle = 10
            inner_later = 5
            ua = ""
            content = 0
            content_length = 0
            referer = 1
            apiEventList = self.get_api(api_list, tm, ip, ua, content, user, outer_circle, outer_later, content_length,
                                        inner_circle,
                                        inner_later, referer)
            return apiEventList

        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []

    def runDayAmountLargeOverNormal(self, tm, ip, user):
        try:
            # tm = formatToTime("%s 10:40:00" % (date))
            tm = tm + 3600 * 10 + 2400

            listParams = self.getApiConfig("allCustomer")
            detailParams = self.getApiConfig("customerDetail")

            # 然后分页获取用户信息列表，然后获取用户详情
            apiEventList = []
            # 获取列表和获取详情
            for i in range(200):
                tm += 1
                listParams["tm"] = tm
                listParams["ip"] = ip
                listParams[
                    "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                res = self.getApiEventTemplate(listParams)
                apiEventList.append(res)

                for k in range(10):
                    tm += 5
                    detailParams["tm"] = tm
                    detailParams["ip"] = ip
                    detailParams[
                        "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                    res = self.getApiEventTemplate(detailParams)
                    apiEventList.append(res)
                    # end for
            # end for

            return apiEventList
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []
            # end try

    # end def


    def runDayLabelCountOverNormal_currency(self, tm, ip, user):
        try:
            tm = tm + 3600 * 10 + 3000
            api_list = {"customerDetail": 1, "shopAbroad": 1, "allCustomer": 1}
            outer_circle = 200
            outer_later = 1
            inner_circle = 10
            inner_later = 5
            ua = ""
            content = 1
            content_length = 50
            referer = 1
            apiEventList = self.get_api(api_list, tm, ip, ua, content, user, outer_circle, outer_later, content_length,
                                        inner_circle,
                                        inner_later, referer)
            return apiEventList

        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []

    def runDayLabelCountOverNormal(self, tm, ip, user):
        try:
            # tm = formatToTime("%s 10:50:00" % (date))
            tm = tm + 3600 * 10 + 3000

            listParams = self.getApiConfig("allCustomer")
            detailParams = self.getApiConfig("customerDetail")

            # 然后分页获取用户信息列表，然后获取用户详情
            apiEventList = []
            # 获取列表和获取详情
            for i in range(20):
                tm += 1
                listParams["tm"] = tm
                listParams["ip"] = ip
                listParams[
                    "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

                listBody = "{\"success\": true, \"data\":["
                for j in range(10):
                    listBody += "{\"user\": \"晓红\", \"phone\": \"%d\", \"email\": \"%d@163.com\", \"card\":\"6227002470170278192\", \"pid\": \"320481199004101010\"}," % (
                    15365019832 + i + j, 15365019832 + i + j)
                # end for
                listBody = listBody[0:-1]
                listBody += "]}"

                listParams["body"] = listBody
                res = self.getApiEventTemplate(listParams)
                apiEventList.append(res)

                for k in range(10):
                    tm += 5
                    detailParams["tm"] = tm
                    detailParams["ip"] = ip
                    detailParams[
                        "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

                    detailBody = "{\"success\": true, \"data\":"
                    detailBody += "{\"user\": \"晓红\", \"phone\": \"%d\", \"email\": \"%d@163.com\", \"card\":\"6227002470170278192\", \"pid\": \"320481199004101010\"}" % (
                    15365019832 + i + k, 15365019832 + i + k)
                    detailBody += "}"

                    detailParams["body"] = detailBody

                    res = self.getApiEventTemplate(detailParams)
                    apiEventList.append(res)
                    # end for
            # end for

            return apiEventList
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []
            # end try

    # end def

    def runDayLabelCountLargeOverNormal_currency(self, tm, ip, user):
        try:
            tm = tm + 3600 * 10 + 1800
            api_list = {"customerDetail": 1, "shopAbroad": 1, "allCustomer": 1}
            outer_circle = 700
            outer_later = 1
            inner_circle = 1
            inner_later = 5
            ua = ""
            content = 1
            content_length = 150
            referer = 1
            apiEventList = self.get_api(api_list, tm, ip, ua, content, user, outer_circle, outer_later,
                                        content_length, inner_circle,
                                        inner_later, referer)
            return apiEventList

        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []

    def runDayLabelCountLargeOverNormal(self, tm, ip, user):
        try:
            # tm = formatToTime("%s 10:30:00" % (date))
            tm = tm + 3600 * 10 + 1800

            listParams = self.getApiConfig("allCustomer")
            detailParams = self.getApiConfig("customerDetail")

            # 然后分页获取用户信息列表，然后获取用户详情
            apiEventList = []
            # 获取列表和获取详情
            for i in range(1000):
                tm += 1
                listParams["tm"] = tm
                listParams["ip"] = ip
                listParams[
                    "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

                listBody = "{\"success\": true, \"data\":["
                for j in range(100):
                    listBody += "{\"user\": \"晓红\", \"phone\": \"%d\", \"email\": \"%d@163.com\", \"card\":\"6227002470170278192\", \"pid\": \"320481199004101010\"}," % (
                    15365017832 + i + j, 15362019832 + i + j)
                # end for
                listBody = listBody[0:-1]
                listBody += "]}"

                listParams["body"] = listBody
                res = self.getApiEventTemplate(listParams)
                apiEventList.append(res)

                for k in range(1):
                    tm += 5
                    detailParams["tm"] = tm
                    detailParams["ip"] = ip
                    detailParams[
                        "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

                    detailBody = "{\"success\": true, \"data\":"
                    detailBody += "{\"user\": \"晓红\", \"phone\": \"%d\", \"email\": \"%d@163.com\", \"card\":\"6227002470170278192\", \"pid\": \"320481199004101010\"}" % (
                    15365018832 + i + k, 15325019832 + i + k)
                    detailBody += "}"

                    detailParams["body"] = detailBody

                    res = self.getApiEventTemplate(detailParams)
                    apiEventList.append(res)
                    # end for
            # end for

            return apiEventList
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []
            # end try

    # end def


    def runIpPropsOverNormal_currency(self, tm, ip, user):
        try:
            tm = tm + 3600 * 11
            api_list = {"customerDetail": 1, "shopAbroad": 1, "allCustomer": 1}
            outer_circle = 10
            outer_later = 1
            inner_circle = 10
            inner_later = 5
            ua = ""
            content = 1
            content_length = 30
            referer = 1
            apiEventList = self.get_api(api_list, tm, ip, ua, content, user, outer_circle, outer_later,
                                        content_length, inner_circle,
                                        inner_later, referer)
            return apiEventList

        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []

    def runIpPropsOverNormal(self, tm, ip, user):
        try:
            # tm = formatToTime("%s 11:00:00" % (date))
            tm = tm + 3600 * 11

            listParams = self.getApiConfig("allCustomer")
            detailParams = self.getApiConfig("customerDetail")

            # 然后分页获取用户信息列表，然后获取用户详情
            apiEventList = []
            # 获取列表和获取详情
            for i in range(10):
                tm += 1
                listParams["tm"] = tm
                listParams["ip"] = ip
                listParams[
                    "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

                listBody = "{\"success\": true, \"data\":["
                for j in range(30):
                    listBody += "{\"user\": \"晓红\", \"phone\": \"%d\", \"email\": \"%d@163.com\", \"card\":\"6227002470170278192\", \"pid\": \"320481199004101010\"}," % (
                    15365019832 + i + j, 15365019832 + i + j)
                # end for
                listBody = listBody[0:-1]
                listBody += "]}"

                listParams["body"] = listBody
                res = self.getApiEventTemplate(listParams)
                apiEventList.append(res)

                for k in range(10):
                    tm += 5
                    detailParams["tm"] = tm
                    detailParams["ip"] = ip
                    detailParams[
                        "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

                    detailBody = "{\"success\": true, \"data\":"
                    detailBody += "{\"user\": \"晓红\", \"phone\": \"%d\", \"email\": \"%d@163.com\", \"card\":\"6227002470170278192\", \"pid\": \"320481199004101010\"}" % (
                    15365019832 + i + k, 15365019832 + i + k)
                    detailBody += "}"

                    detailParams["body"] = detailBody

                    res = self.getApiEventTemplate(detailParams)
                    apiEventList.append(res)
                    # end for
            # end for


            return apiEventList
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []
            # end try

    # end def


    def runLabelCountPreOverNormal_currency(self, tm, ip, user):
        try:
            # tm = formatToTime("%s 11:10:00" % (date))
            tm = tm + 3600 * 11 + 600
            api_list = {"customerDetail": 0, "shopAbroad": 0, "allCustomer": 1}
            outer_circle = 3
            outer_later = 12
            inner_circle = 1
            inner_later = 1
            ua = ""
            content = 1
            content_length = 900
            referer = 1
            apiEventList = self.get_api(api_list, tm, ip, ua, content, user, outer_circle, outer_later,
                                        content_length, inner_circle,
                                        inner_later, referer)
            return apiEventList

        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []

    def runLabelCountPreOverNormal(self, tm, ip, user):
        try:
            # tm = formatToTime("%s 11:10:00" % (date))
            tm = tm + 3600 * 11 + 600

            listParams = self.getApiConfig("allCustomer")
            detailParams = self.getApiConfig("customerDetail")

            # 然后分页获取用户信息列表，然后获取用户详情
            apiEventList = []
            # 获取列表和获取详情
            for i in range(5):
                tm += 12
                listParams["tm"] = tm
                listParams["ip"] = ip
                listParams[
                    "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

                listBody = "{\"success\": true, \"data\":["
                for j in range(200):
                    listBody += "{\"user\": \"晓红\", \"phone\": \"%d\", \"email\": \"%d@163.com\", \"card\":\"6227002470170278192\", \"pid\": \"320481199004101010\"}," % (
                    15365019832 + i + j, 15365019832 + i + j)
                # end for
                listBody = listBody[0:-1]
                listBody += "]}"

                listParams["body"] = listBody
                res = self.getApiEventTemplate(listParams)
                apiEventList.append(res)
            # end for

            return apiEventList
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []
            # end try

    # end def



    def runAmountFreOverNormal_currency(self, tm, ip, user):
        try:
            # tm = formatToTime("%s 11:10:00" % (date))
            tm = tm + 3600 * 11 + 1200
            api_list = {"customerDetail": 0, "shopAbroad": 0, "allCustomer": 1}
            outer_circle = 40
            outer_later = 0.5
            inner_circle = 1
            inner_later = 1
            ua = ""
            content = 1
            content_length = 10
            referer = 1
            apiEventList = self.get_api(api_list, tm, ip, ua, content, user, outer_circle, outer_later,
                                        content_length, inner_circle,
                                        inner_later, referer)
            return apiEventList

        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []

    def runAmountFreOverNormal(self, tm, ip, user):
        try:
            # tm = formatToTime("%s 11:20:00" % (date))
            tm = tm + 3600 * 11 + 1200

            listParams = self.getApiConfig("allCustomer")
            detailParams = self.getApiConfig("customerDetail")

            # 然后分页获取用户信息列表，然后获取用户详情
            apiEventList = []
            # 获取列表和获取详情
            for i in range(10):
                tm += 0.5
                listParams["tm"] = tm
                listParams["ip"] = ip
                listParams[
                    "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

                listBody = "{\"success\": true, \"data\":["
                for j in range(10):
                    listBody += "{\"user\": \"晓红\", \"phone\": \"%d\", \"email\": \"%d@163.com\", \"card\":\"6227002470170278192\", \"pid\": \"320481199004101010\"}," % (
                    15365019832 + i + j, 15365019832 + i + j)
                # end for
                listBody = listBody[0:-1]
                listBody += "]}"

                listParams["body"] = listBody
                res = self.getApiEventTemplate(listParams)
                apiEventList.append(res)
            # end for

            return apiEventList
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []
            # end try

    # end def

    def runApiRouteOverNormal_currency(self, tm, ip, user):
        try:
            # tm = formatToTime("%s 11:10:00" % (date))
            tm = tm + 3600 * 11 + 1800
            api_list = {"customerDetail": 1, "shopAbroad": 1, "allCustomer": 0}
            outer_circle = 20
            outer_later = 1
            inner_circle = 10
            inner_later = 5
            ua = ""
            content = 1
            content_length = 1
            referer = 1
            apiEventList = self.get_api(api_list, tm, ip, ua, content, user, outer_circle, outer_later,
                                        content_length, inner_circle,
                                        inner_later, referer)
            return apiEventList

        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []

    def runApiRouteOverNormal(self, tm, ip, user):
        try:
            # tm = formatToTime("%s 11:30:00" % (date))
            tm = tm + 3600 * 11 + 1800

            listParams = self.getApiConfig("allCustomer")
            detailParams = self.getApiConfig("customerDetail")

            # 然后分页获取用户信息列表，然后获取用户详情
            apiEventList = []
            # 获取列表和获取详情
            for i in range(20):
                tm += 1

                for k in range(10):
                    tm += 5
                    detailParams["tm"] = tm
                    detailParams["ip"] = ip
                    detailParams[
                        "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

                    detailBody = "{\"success\": true, \"data\":"
                    detailBody += "{\"user\": \"晓红\", \"phone\": \"%d\", \"email\": \"%d@163.com\", \"card\":\"6227002470170278392\", \"pid\": \"320481198004101010\"}" % (
                    15363019832 + i + k, 15325019832 + i + k)
                    detailBody += "}"

                    detailParams["body"] = detailBody

                    res = self.getApiEventTemplate(detailParams)
                    apiEventList.append(res)
                    # end for
            # end for

            return apiEventList
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []
            # end try

    # end def





    def runCirclrAmount_currency(self, tm, ip, user):
        try:
            # tm = formatToTime("%s 11:10:00" % (date))
            tm = tm + 3600 * 11 + 400
            api_list = {"customerDetail": 1, "shopAbroad": 1, "allCustomer": 1}
            outer_circle = 70
            outer_later = 10
            inner_circle = 20
            inner_later = 5
            ua = ""
            content = 1
            content_length = 30
            referer = 1
            apiEventList = self.get_api(api_list, tm, ip, ua, content, user, outer_circle, outer_later,
                                        content_length, inner_circle,
                                        inner_later, referer)
            return apiEventList

        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []
            # end try

    # end def


    def runCirclrAmount(self, tm, ip, user):
        try:
            # tm = formatToTime("%s 11:50:00" % (date))
            tm = tm + 3600 * 11 + 3000

            listParams = self.getApiConfig("allCustomer")
            detailParams = self.getApiConfig("customerDetail")

            # 然后分页获取用户信息列表，然后获取用户详情
            apiEventList = []
            # 获取列表和获取详情
            for i in range(10):
                tm += 10
                listParams["tm"] = tm
                listParams["ip"] = ip
                listParams[
                    "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

                listBody = "{\"success\": true, \"data\":["
                for j in range(30):
                    listBody += "{\"user\": \"晓红\", \"phone\": \"%d\", \"email\": \"%d@163.com\", \"card\":\"6227002470170278192\", \"pid\": \"320481199004101010\"}," % (
                    15365019832 + i + j, 15365019832 + i + j)
                # end for
                listBody = listBody[0:-1]
                listBody += "]}"

                listParams["body"] = listBody
                res = self.getApiEventTemplate(listParams)
                apiEventList.append(res)

                for k in range(10):
                    tm += 5
                    detailParams["tm"] = tm
                    detailParams["ip"] = ip
                    detailParams[
                        "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

                    detailBody = "{\"success\": true, \"data\":"
                    detailBody += "{\"user\": \"晓红\", \"phone\": \"%d\", \"email\": \"%d@163.com\", \"card\":\"6227002470170278192\", \"pid\": \"320481199004101010\"}" % (
                    15365019832 + i + k, 15365019832 + i + k)
                    detailBody += "}"

                    detailParams["body"] = detailBody

                    res = self.getApiEventTemplate(detailParams)
                    apiEventList.append(res)
                    # end for
            # end for

            return apiEventList
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []
            # end try

    # end def


    def runCookieUseIps_currency(self, tm, user, ipList):
        try:
            # tm = formatToTime("%s 11:10:00" % (date))
            tm = tm + 3600 * 10
            api_list = {"customerDetail": 1, "shopAbroad": 1, "allCustomer": 1}
            outer_circle = 5
            outer_later = 10
            inner_circle = 10
            inner_later = 5
            ua = ""
            content = 1
            content_length = 30
            apiEventLists = []
            referer = 1
            for ip in ipList:
                apiEventList = self.get_api(api_list, tm, ip, ua, content, user, outer_circle, outer_later,
                                            content_length, inner_circle,
                                            inner_later, referer)
                apiEventLists += apiEventList
            return apiEventLists

        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []
            # end try

    # end def


    def runCookieUseIps(self, tm, user, ipList):
        try:
            # tm = formatToTime("%s 10:00:00" % (date))
            tm = tm + 3600 * 10

            listParams = self.getApiConfig("allCustomer")
            detailParams = self.getApiConfig("customerDetail")

            apiEventList = []
            for ip in ipList:
                for i in range(5):
                    tm += 10
                    listParams["tm"] = tm
                    listParams["ip"] = ip
                    listParams[
                        "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

                    listBody = "{\"success\": true, \"data\":["
                    for j in range(30):
                        listBody += "{\"user\": \"晓红\", \"phone\": \"%d\", \"email\": \"%d@163.com\", \"card\":\"6227002470170278192\", \"pid\": \"320481199004101010\"}," % (
                        15365019832 + i + j, 15365019832 + i + j)
                    # end for
                    listBody = listBody[0:-1]
                    listBody += "]}"

                    listParams["body"] = listBody
                    res = self.getApiEventTemplate(listParams)
                    apiEventList.append(res)

                    for k in range(10):
                        tm += 5
                        detailParams["tm"] = tm
                        detailParams["ip"] = ip
                        detailParams[
                            "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

                        detailBody = "{\"success\": true, \"data\":"
                        detailBody += "{\"user\": \"晓红\", \"phone\": \"%d\", \"email\": \"%d@163.com\", \"card\":\"6227002470170278192\", \"pid\": \"320481199004101010\"}" % (
                        15365019832 + i + k, 15365019832 + i + k)
                        detailBody += "}"

                        detailParams["body"] = detailBody

                        res = self.getApiEventTemplate(detailParams)
                        apiEventList.append(res)
                        # end for
                        # end for
            # end for

            return apiEventList
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []
            # end try

    # end def



    def runIpRangeExcept_currency(self, tm, user, ip):
        try:
            # tm = formatToTime("%s 11:10:00" % (date))
            tm = tm + 3600 * 14
            api_list = {"customerDetail": 1, "shopAbroad": 1, "allCustomer": 0}
            outer_circle = 1
            outer_later = 1
            inner_circle = 30
            inner_later = 5
            ua = ""
            content = 0
            content_length = 0
            referer = 1
            apiEventList = self.get_api(api_list, tm, ip, ua, content, user, outer_circle, outer_later,
                                        content_length, inner_circle,
                                        inner_later, referer)
            return apiEventList

        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []
            # end try
            # end def

    def runIpRangeExcept(self, tm, user, ip):
        try:
            # tm = formatToTime("%s 14:00:00" % (date))
            tm = tm + 3600 * 14

            listParams = self.getApiConfig("allCustomer")
            detailParams = self.getApiConfig("customerDetail")

            apiEventList = []

            for k in range(30):
                tm += 5
                detailParams["tm"] = tm
                detailParams["ip"] = ip
                detailParams[
                    "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

                detailBody = "{\"success\": true, \"data\":"
                detailBody += "{\"user\": \"晓红\", \"phone\": \"%d\", \"email\": \"%d@163.com\", \"card\":\"6227002470170278192\", \"pid\": \"320481199004101010\"}" % (
                15365019832 + k, 15365019832 + k)
                detailBody += "}"

                detailParams["body"] = detailBody

                res = self.getApiEventTemplate(detailParams)
                apiEventList.append(res)
            # end for

            return apiEventList
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []
            # end try

    # end def



    # def runOneByOne_currency(self,tm, user, ip, count):
    #     try:
    #         # tm = formatToTime("%s 11:10:00" % (date))
    #         tm = tm + 3600 * 14
    #         api_list = {"customerDetail": 1, "shopAbroad": 1, "allCustomer": 0}
    #         outer_circle = 1
    #         outer_later = 1
    #         inner_circle = 30
    #         inner_later = 5
    #         ua = ""
    #         content = 0
    #         content_length = 0
    #         apiEventList = self.get_api(self, api_list, tm, ip, ua, content, user, outer_circle, outer_later,
    #                                     content_length, inner_circle,
    #                                     inner_later)
    #         return apiEventList
    #
    #     except Exception, e:
    #         self.error(str(e), getCurrentFunctionName())
    #         return []
    def runOneByOne(self, tm, user, ip, count):
        try:
            # tm = formatToTime("%s 10:30:00" % (date))
            tm = tm + 3600 * 10 + 1800

            loginParams = self.getApiConfig("login")
            listParams = self.getApiConfig("allCustomer")
            detailParams = self.getApiConfig("customerDetail")

            apiEventList = []

            for i in range(count):
                tm += 2
                loginParams["tm"] = tm
                loginParams["ip"] = ip
                loginParams["postParams"] = {
                    "validate": "login",
                    "userId": user,
                    "password": "admin123456"
                }
                loginParams[
                    "setCookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                res = self.getApiEventTemplate(loginParams)
                apiEventList.append(res)

                tm += 2
                listParams["tm"] = tm
                listParams["ip"] = ip
                listParams[
                    "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                res = self.getApiEventTemplate(listParams)
                listBody = "{\"success\": true, \"data\":["
                for j in range(30):
                    listBody += "{\"user\": \"晓红\", \"phone\": \"%d\", \"email\": \"%d@163.com\", \"card\":\"6227002470170278192\", \"pid\": \"320481199004101010\"}," % (
                    15365019832 + i + j, 15365019832 + i + j)
                # end for
                listBody = listBody[0:-1]
                listBody += "]}"
                listParams["body"] = listBody
                apiEventList.append(res)

                tm += 2
                detailParams["tm"] = tm
                detailParams["ip"] = ip
                detailParams[
                    "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                res = self.getApiEventTemplate(detailParams)
                detailBody = "{\"success\": true, \"data\":"
                detailBody += "{\"user\": \"晓红\", \"phone\": \"%d\", \"email\": \"%d@163.com\", \"card\":\"6227002470170278192\", \"pid\": \"320481199004101010\"}" % (
                15365019832 + i, 15365019832 + i)
                detailBody += "}"
                detailParams["body"] = detailBody
                apiEventList.append(res)
            # end for

            return apiEventList
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []
            # end try

    # end def


    # def runReferer_currency(self, tm, user, ip):
    #     try:
    #         # tm = formatToTime("%s 11:10:00" % (date))
    #         tm = tm + 3600 * 10 + 1800
    #         api_list = {"customerDetail": 1, "shopAbroad": 1, "allCustomer": 1,"login":1}
    #         outer_circle = 1
    #         outer_later = 1
    #         inner_circle = 30
    #         inner_later = 5
    #         ua = ""
    #         content = 0
    #         content_length = 0
    #         apiEventList = self.get_api(self, api_list, tm, ip, ua, content, user, outer_circle, outer_later,
    #                                     content_length, inner_circle,
    #                                     inner_later)
    #         return apiEventList
    #
    #     except Exception, e:
    #         self.error(str(e), getCurrentFunctionName())
    #         return []
    def runReferer_currency(self, tm, user, ip):
        try:
            tm = tm + 3600 * 10 + 1800

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
            loginParams[
                "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            res = self.getApiEventTemplate(loginParams)
            apiEventList.append(res)

            api_list = {"customerDetail": 1, "shopAbroad": 1, "allCustomer": 1, "login": 1}
            outer_circle = 1
            outer_later = 1
            inner_circle = 10
            inner_later = 0.5
            ua = ""
            content = 0
            content_length = 0
            referer = ""
            apiEventList = self.get_api(api_list, tm, ip, ua, content, user, outer_circle, outer_later,
                                        content_length, inner_circle,
                                        inner_later, referer)
            return apiEventList
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []
            # end try

    # end def

    def runReferer(self, tm, user, ip):
        try:
            tm = tm + 3600 * 10 + 1800

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
            loginParams[
                "setCookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            res = self.getApiEventTemplate(loginParams)
            apiEventList.append(res)

            # 2、获取列表和获取详情
            for i in range(1):
                tm += 1
                listParams["tm"] = tm
                listParams["ip"] = ip
                listParams["referer"] = ""
                listParams[
                    "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                res = self.getApiEventTemplate(listParams)
                apiEventList.append(res)

                for k in range(10):
                    tm += 0.5
                    detailParams["tm"] = tm
                    detailParams["ip"] = ip
                    detailParams["referer"] = ""
                    detailParams[
                        "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                    res = self.getApiEventTemplate(detailParams)
                    apiEventList.append(res)
                    # end for
            # end for

            return apiEventList
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []
            # end try

    # end def

    def runExceptTime(self, tm, user, ip):
        try:
            tm = tm + 3600 * 1

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
            loginParams[
                "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            res = self.getApiEventTemplate(loginParams)
            apiEventList.append(res)

            # 2、获取列表和获取详情
            for i in range(10):
                tm += 2
                listParams["tm"] = tm
                listParams["ip"] = ip
                listParams["referer"] = ""
                listParams[
                    "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                res = self.getApiEventTemplate(listParams)
                apiEventList.append(res)

                for k in range(30):
                    tm += 2
                    detailParams["tm"] = tm
                    detailParams["ip"] = ip
                    detailParams["referer"] = ""
                    detailParams[
                        "cookie"] = "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID=" + user + "; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                    res = self.getApiEventTemplate(detailParams)
                    apiEventList.append(res)
                    # end for
            # end for

            return apiEventList
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            return []
            # end try

    # end def

    def send(self, apiEventList):
        try:
            if apiEventList is None or len(apiEventList) < 1:
                return
            # end if

            client = KafkaClient(hosts=self.hosts)
            topic = client.topics["ApiEvents"]
            producer = topic.get_sync_producer()

            for row in apiEventList:
                msg = json.write(row)
                # print msg
                producer.produce(msg)
                # end for

        except Exception, e:
            self.error(str(e), getCurrentFunctionName())
            # end try

    # end def

    def run(self):
        try:
            apiEventList = []
            if self.threadName == "normal":
                pass
            elif self.threadName == "runLoginCrashPwd":
                # 登录的暴力破解
                apiEventList = self.runLoginCrashPwd(self.tm, "192.168.0.101", "cyefuc")
            elif self.threadName == "runLogin":
                # 刷库
                apiEventList = self.runLogin(self.tm, "192.168.0.102",
                                             ['htoedi', 'ayvzyf', 'hvixhx', 'gotbiq', 'ukeqqx', 'hwvuat', 'ewlwrt',
                                              'xxjxzo', 'uibixg', 'qlgwas', 'gbrpfa', 'qgplcx', 'rjvodk', 'siipeo',
                                              'myquzl', 'thwyrq', 'towlik', 'unqzdk', 'qtmvpm', 'zmefsx', 'nhvtmg',
                                              'ztqysq', 'kucgtz', 'regsbx', 'ugfqok', 'cyefuc', 'pagirc', 'xmdupy',
                                              'urhzfi', 'odyzcj', 'youvbt', 'mdllxc', 'bdpppl', 'jxzcdg', 'cdulmn',
                                              'seyvbv', 'ufcvmw', 'ujrsav', 'niqxos', 'excgsh', 'yyvxck', 'xkqlwe',
                                              'uffmip', 'zkinmv', 'dpirju', 'tlchtn', 'wfxipx', 'zzszvy', 'oktgtn',
                                              'qcueut', 'hufzma', 'cqtuco', 'qjaqno', 'qvtqoh', 'ikdqux', 'uocryb',
                                              'qmnaah', 'xvghdc', 'onllzl', 'uuahir', 'rdadkg', 'gwfakc', 'qxdaoh',
                                              'acvtyg', 'hyjksl', 'zbryvu', 'zletbq', 'noowmw', 'wfcbgk', 'wegyle',
                                              'timhgl', 'nozfke', 'lueglj', 'khvcku', 'vzcqhf', 'uptsox', 'vgufoq',
                                              'jevmqt', 'tevmar', 'geggsb', 'lfpbqi', 'wsfluz', 'nkcdoh', 'lqqbiu',
                                              'qztxal', 'fymzqv', 'blpsix', 'pciwpv', 'kfypnp', 'vgsyvt', 'stmzzg',
                                              'teocti', 'jrmhzi', 'jmgtlx', 'hrxbct', 'onfywk', 'pjodll', 'vmpnjg',
                                              'vifihu', 'bjmuan', 'xqvdcx', 'zwucdz', 'lwvluv', 'ypkehk', 'ecwiit',
                                              'kmlzue', 'pxgatz', 'fmvwnd', 'fdahgf', 'zmwpdj', 'wfhkbf', 'tboxpy',
                                              'fcitcu', 'oiswkn', 'mxjmmf', 'mbdalb', 'zgealm', 'paavjt', 'oxezvc',
                                              'vbpuox', 'qsuklu', 'fgiicg', 'ebikiw', 'stftgq', 'hvsjwm', 'loogpz',
                                              'dpdlyz', 'fdjpxv', 'bpebjp', 'msomwz', 'fbftcv', 'jdahqu', 'ggbjlw',
                                              'ypiugj'])
            elif self.threadName == "runUa":
                # 出现异常UA
                apiEventList = self.runUa_currency(self.tm, "192.168.0.100", "hvixhx", "Python-httplib2/2.7 (gzip)")
            elif self.threadName == "runReferer":
                # 异常Referer
                apiEventList = self.runReferer_currency(self.tm, "cqtuco", "192.168.4.34")
            elif self.threadName == "ipOverUserCount":
                # 同IP多账号异常
                apiEventList.extend(self.runNormal(self.tm, "192.168.6.101", "qgplcx"))
                apiEventList.extend(self.runNormal(self.tm, "192.168.6.101", "rjvodk"))
                apiEventList.extend(self.runNormal(self.tm, "192.168.6.101", "siipeo"))
                apiEventList.extend(self.runNormal(self.tm, "192.168.6.101", "ypiugj"))
                apiEventList.extend(self.runNormal(self.tm, "192.168.6.101", "ggbjlw"))
                apiEventList.extend(self.runNormal(self.tm, "192.168.6.101", "jdahqu"))
                apiEventList.extend(self.runNormal(self.tm, "192.168.6.101", "fbftcv"))
                apiEventList.extend(self.runNormal(self.tm, "192.168.6.101", "fcitcu"))
                apiEventList.extend(self.runNormal(self.tm, "192.168.6.101", "tboxpy"))
                apiEventList.extend(self.runNormal(self.tm, "192.168.6.101", "wfhkbf"))
                apiEventList.extend(self.runNormal(self.tm, "192.168.6.101", "zmwpdj"))
                apiEventList.extend(self.runNormal(self.tm, "192.168.6.101", "fdahgf"))
                apiEventList.extend(self.runNormal(self.tm, "192.168.6.101", "fmvwnd"))
                apiEventList.extend(self.runNormal(self.tm, "192.168.6.101", "pxgatz"))
                apiEventList.extend(self.runNormal(self.tm, "192.168.6.101", "kmlzue"))
                apiEventList.extend(self.runNormal(self.tm, "192.168.6.101", "ecwiit"))
                apiEventList.extend(self.runNormal(self.tm, "192.168.6.101", "ypkehk"))
                apiEventList.extend(self.runNormal(self.tm, "192.168.6.101", "lwvluv"))
                apiEventList.extend(self.runNormal(self.tm, "192.168.6.101", "zwucdz"))
                apiEventList.extend(self.runNormal(self.tm, "192.168.6.101", "xqvdcx"))
                apiEventList.extend(self.runNormal(self.tm, "192.168.6.101", "bjmuan"))
            # elif self.threadName == "dayAmountOverNormal":
            #     # 日访问次数偏移用户基线
            #     apiEventList = self.runDayAmountOverNormal_currency(self.tm, "192.168.2.10", "gotbiq")
            elif self.threadName == "dayAmountLargeOverNormal":
                # 日访问次数大幅偏移用户基线
                apiEventList = self.runDayAmountLargeOverNormal_currency(self.tm, "192.168.3.22", "ukeqqx")
            # elif self.threadName == "dayLabelCountOverNormal":
            #     # 日敏感标签访问量偏移用户基线
            #     apiEventList = self.runDayLabelCountOverNormal_currency(self.tm, "192.168.4.34", "hwvuat")
            elif self.threadName == "dayLabelCountLargeOverNormal":
                # 日敏感标签访问量大幅偏移用户基线
                apiEventList = self.runDayLabelCountLargeOverNormal_currency(self.tm, "192.168.5.50", "ewlwrt")
            # elif self.threadName == "ipPropsOverNormal":
            #     使用IP属性偏移用户基线
                # apiEventList = self.runIpPropsOverNormal_currency(self.tm, "220.184.86.203", "xxjxzo")
            elif self.threadName == "ipPropsLargeOverNormal":
                # 使用IP属性大幅偏移用户基线
                apiEventList = self.runIpPropsOverNormal_currency(self.tm, "220.184.86.203", "uibixg")
                apiEventList.extend(self.runIpPropsOverNormal_currency(self.tm, "211.134.100.100", "uibixg"))
                apiEventList.extend(self.runIpPropsOverNormal_currency(self.tm, "56.23.52.41", "uibixg"))
            elif self.threadName == "ipCountOverNormal":
                # 使用IP数量偏移用户基线
                apiEventList = self.runNormal(self.tm, "192.168.6.101", "qlgwas")
                apiEventList.extend(self.runNormal(self.tm, "192.168.6.200", "qlgwas"))
                apiEventList.extend(self.runNormal(self.tm, "192.168.6.40", "qlgwas"))
            elif self.threadName == "circlrAmount":
                # 是否周期性访问异常
                apiEventList = self.runCirclrAmount_currency(self.tm, "192.168.4.34", "gbrpfa")
            elif self.threadName == "labelCountPreOverNormal":
                # 单次请求数据量偏离基线
                apiEventList = self.runLabelCountPreOverNormal_currency(self.tm, "192.168.7.120", "thwyrq")
            elif self.threadName == "amountFreOverNormal":
                # 请求频次偏移基线
                apiEventList = self.runAmountFreOverNormal_currency(self.tm, "192.168.8.141", "unqzdk")
            elif self.threadName == "apiRouteOverNormal":
                # 接口请求路径偏离基线
                apiEventList = self.runApiRouteOverNormal_currency(self.tm, "192.168.4.34", "zmefsx")
            elif self.threadName == "cookieUseIps":
                # 同一个Cookie在不同的IP上使用
                apiEventList = self.runCookieUseIps_currency(self.tm, "myquzl",
                                                             ["192.168.0.100", "192.168.1.101", "192.168.4.34"])
            elif self.threadName == "ipRangeExcept":
                # IP地址段异常，出现以前没出现过的IP段
                apiEventList = self.runIpRangeExcept_currency(self.tm, "cqtuco", "10.10.0.159")
            elif self.threadName == "exceptTime":
                # 异常时间段
                apiEventList = self.runExceptTime(self.tm, "gwfakc", "10.97.13.93")
            elif self.threadName == "oneByOne":
                apiEventList = self.runOneByOne(self.tm, "cqtuco", "10.10.0.159", 10)
            self.send(apiEventList)
        except Exception, e:
            self.error(str(e), getCurrentFunctionName())


def main(hosts, time_str):
    try:
        # threadNameList = ["runLogin", "runReferer",  "cookieUseIps", "runLoginCrashPwd","runUa"
        #                    "circlrAmount"]
        threadNameList = ["runLogin", "runReferer", "ipRangeExcept", "cookieUseIps", "runLoginCrashPwd",
                          "runUa", "dayAmountOverNormal", "dayAmountLargeOverNormal", "dayLabelCountOverNormal",
                          "dayLabelCountLargeOverNormal", "ipPropsOverNormal", "ipPropsLargeOverNormal",
                          "ipCountOverNormal", "circlrAmount", "ipOverUserCount", "labelCountPreOverNormal",
                          "amountFreOverNormal", "apiRouteOverNormal", "exceptTime"]
        # threadNameList = ["dayLabelCountLargeOverNormal"]

        tm = formatToTime(time_str)
        threadList = []
        for threadName in threadNameList:
            t = Spider(threadName, hosts, tm)
            threadList.append(t)
        # end for

        for t in threadList:
            t.start()
        # end for

        for t in threadList:
            t.join()
            # end for

    except Exception, e:
        print str(e)

# 验证12种风险是否已经触发
def assertRisk(ip, riskTumple):
    mongo_client = pymongo.MongoClient(ip, 27017)
    db = mongo_client["audit"]
    db.authenticate("audit", "123@Audit")
    collection = db.get_collection("riskInfo")
    for risk in riskTumple:
        doucment = collection.find({u"risk": risk})
        if doucment.count() != 0:
            print(risk.decode('utf8') + "--成功触发,触发次数为：" + str(doucment.count()) + "次")
            continue
        else:
            for item in range(10):
                doucment = collection.find({u"risk": risk})
                if doucment.count() != 0:
                    print(risk.decode('utf8') + "--成功触发,触发次数为：" + str(doucment.count()) + "次")
                    break
                else:
                    time.sleep(1)
                    # print("查询" + str(item+1) + "次")
                    if item + 1 == 10:
                        print(risk.decode('utf8') + "--没有触发")
                        break


if __name__ == '__main__':
    initLog(logging.DEBUG, logging.DEBUG, "logs/" + os.path.split(__file__)[1].split(".")[0] + ".log")
    if len(sys.argv) != 4:
        print "argv error, RiskTest.py ip startDay lenPlan"
        sys.exit(1)
    ip = sys.argv[1]
    startDay = sys.argv[2]
    lenPlan = sys.argv[3]
    # ip="192.168.0.60"
    # startDay = "2018-10-09"
    # lenPlan=8
    threadNum=10
    hosts = ip+":9093"
    toolUtils = ToolUtils()
    timeStamp = toolUtils.timeStrToTimeStamp(startDay,"%Y-%m-%d") + int(lenPlan)*24*60*60
    delayDay = toolUtils.timeStmpToTimeStr(timeStamp,"%Y-%m-%d")
    riskTumple = (
    u"IP异常", u"获取敏感数据量大幅偏移基线", u"请求频次偏移基线", u"周期性访问风险", u"请求路径异常",
    u"请求使用浏览器头异常", u"单次请求数据量风险", u"Cookie盗用", u"账号暴力破解",u"刷库", u"访问时间异常",
    u"账号接口请求次数大幅偏移账号基线",u"用户日访问敏感接口次数大于20次")

    # 1、判断风险策略是否都启动，如果没有启动则启用

    for riskRule in riskTumple:
        if not MongoUtils("RiskTest.py").isStarted(ip,riskRule):
            MongoUtils("RiskTest.py").starRisk(ip,riskRule)
    # 2、配置风险接口、并发送风险数据
    start_mongo_config(hosts)
    #发送正常数据
    main_norml(hosts, threadNum, startDay, lenPlan)
    # #3、跑异常，之前先跑Normal
    main(hosts, delayDay+" 00:00:00")
    # 3、验证风险是否触发
    assertRisk(ip,riskTumple)
