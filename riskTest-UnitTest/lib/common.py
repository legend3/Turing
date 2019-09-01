#!/usr/bin/env python
#-*-encoding:UTF-8-*-
import ConfigParser
import re
import logging
import logging.handlers
import sys
import os
import subprocess
import threading
import socket
import struct
import urllib
import urllib2
import httplib
import httplib2
import inspect
import time
import random
import numpy as np
import datetime

from Queue import Queue

def initLog(console_level, file_level, logfile):
    formatter = logging.Formatter('%(name)-12s %(asctime)s %(levelname)-8s %(message)s')
    logging.getLogger().setLevel(0)
    console_log = logging.StreamHandler()
    console_log.setLevel(console_level)
    console_log.setFormatter(formatter)
    file_log = logging.handlers.RotatingFileHandler(logfile,maxBytes=1024*1024,backupCount=2)

    file_log.setLevel(file_level)
    file_log.setFormatter(formatter)

    logging.getLogger().addHandler(file_log)
    logging.getLogger().addHandler(console_log)
#end def

def writeFileLog(msg, module = '', level = 'error'):
    filename = os.path.split(__file__)[1]
    if level == 'debug':
        logging.getLogger().debug('File:' + filename + ', ' + module + ': ' + msg)
    elif level == 'warning':
        logging.getLogger().warning('File:' + filename + ', ' + module + ': ' + msg)
    else:
        logging.getLogger().error('File:' + filename + ', ' + module + ': ' + msg)
    #end if
#end def

def DEBUG(msg):
    module = ""
    writeFileLog(msg, module, 'debug')
#end def

def ERROR(msg):
    module = ""
    writeFileLog(msg, module, 'error')
#end def

def popen(cmd):
    try:
        return subprocess.Popen(cmd,shell=True,close_fds=True,bufsize=-1,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).stdout.readlines()
    except Exception,e:
        print str(e)
        return ''
    #end try
#end def

def getCurrentFunctionName():
    return inspect.stack()[1][3]
#end def

def toStr(msg):
    try:
        return msg.encode('utf-8')
    except Exception,e:
        return ''
    #end try
#end def


def httpRequest(url,method,headers,body,timeout,enable_forward):
    http = httplib2.Http()
    if enable_forward:
        http.follow_redirects = True
    else:
        http.follow_redirects = False
    #end if
    socket.setdefaulttimeout(timeout)
    response, content = http.request(url,method,headers=headers,body=body)
    return response, content
#end def

def checkProcessExist(process):
    try:
        result = popen("ps -ef | grep %s | grep -v grep | wc -l" % process)
        if result and int(result[0]) > 0:
            return True
        return False
    except Exception,e:
        return False
    #end try
#end def

class Util:
    socketLocker = threading.Lock()
    flowLocker = threading.Lock()
    @classmethod
    def addTimeout(cls,t=5):
        cls.socketLocker.acquire()
        timeout = socket.getdefaulttimeout()
        if timeout:
            if timeout < 115:
                socket.setdefaulttimeout(timeout+t)
        cls.socketLocker.release()
    #end def

    @classmethod
    def subTimeout(cls,t=5):
        cls.socketLocker.acquire()
        timeout = socket.getdefaulttimeout()
        if timeout:
            if timeout > 10:
                socket.setdefaulttimeout(timeout-t)
        cls.socketLocker.release()
    #end def
#end class

def checkIpv4(ip):
    match = re.findall(u"^(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])$",ip,re.I)
    if match and len(match) > 0:
        return True
    else:
        return False
    #end if
#end def

def checkIpv4Inner(ip):
    match = re.findall(u"(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])",ip,re.I)
    if match and len(match) > 0:
        return True
    else:
        return False
    #end if
#end def

def checkIpv4Range(ip_range):
    match = re.findall(u"^(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])-(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])$",ip_range,re.I)
    if match and len(match) > 0:
        return True
    else:
        return False
    #end if
#end def

def checkIpv6(ipv6_addr):
    try:
        addr= socket.inet_pton(socket.AF_INET6, ipv6_addr)
    except socket.error:
        return False
    else:
        return True
    #end try
#end def

def checkIpv6Inner(ipaddr):
    ip = ipaddr.upper()
    match = re.findall(u"((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?",ip,re.I)
    if match and len(match) > 0:
        return True
    else:
        return False
    #end if
#end def

def checkIpv6Domain(domain):
    ip = domain.upper()
    match = re.findall(u"^\[((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\]$",ip,re.I)
    if match and len(match) > 0:
        return True
    else:
        return False
    #end if
#end def

def checkIpv6Range(ip_range):
    try:
        last_colon_index = 0
        tmp = ip_range.split('-')
        if len(tmp) == 2:
            if checkIpv6(tmp[0]):
                if checkIpv6(tmp[1]):
                    return True
                for i in range(len(tmp[0])):
                    if tmp[0][i] == ':':
                        last_colon_index = i
                tmp_line = tmp[0][last_colon_index+1:]
                if len(tmp_line) > len(tmp[1]):
                    return False
                elif len(tmp_line) < len(tmp[1]):
                    return True
                else:
                    if cmp(tmp_line,tmp[1]) <= 0:
                        return True
                    else:
                        return False
            else:
                return False
        else:
            return False
    except Exception, e:
        return False
    #end try
#end def


# 十六进制 to 十进制
def hex2dec(string_num):
    return int(string_num.upper(), 16)
#end def

# 十进制 to 十六进制
def dec2hex(string_num):
    base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num,rem = divmod(num, 16)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])
#end def

def ipv4Toint(addr):
    try:
        return struct.unpack("!I",socket.inet_aton(addr))[0]
    except Exception,e:
        return ''  
    #end try
#end def

def intToipv4(i):
    try:
        return socket.inet_ntoa(struct.pack("!I",i))
    except Exception,e:
        return '' 
    #end try
#end def

def fullIpv6(ip):
    if ip == "" or len(ip) < 4 or len(ip) > 39:
        return False
    #end if
    ip = ip.upper()
    match = re.findall(u"^((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?$",ip,re.I)
    if match and len(match) > 0:
        ip_sep = ip.split(":")
        if len(ip_sep) < 8:
            t = 8 - len(ip_sep)
            ip = ip.replace("::",":"*(t+2))
        #end if
        ip_sep = ip.split(":")
        ip = []
        for row in ip_sep:
            row = "0000%s" % (row)
            ip.append(row[-4:])
        #end for
        ip = ":".join(ip)

        return ip
    else:
        return False
    #end if
#end def

def easyIpv6(ip):
    if ip == "" or len(ip) < 4 or len(ip) > 39:
        return False
    #end if
    ip = ip.lower()
    match = re.findall(u"^((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?$",ip,re.I)
    if match and len(match) > 0:
        ip_sep = ip.split(":")
        ip = []
        for row in ip_sep:
            i = 0
            for i in range(len(row)):
                if row == "":
                    break
                elif row == "0":
                    row = "0"
                    break
                elif row[0] == "0":
                    row = row[1:]
                else:
                    break
                #end if
            #end for
            ip.append(row)
        #end for
        
        if len(ip) == 8:
            ip = ":".join(ip)
            i = 8
            while i > 1:
                index = ip.find(":"+"0:"*i)
                if index > 0:
                    ip = "%s::%s" % (ip[0:index],ip[index+(2*i+1):])
                    break
                #end if
                i -= 1
            #end while
        else:
            ip = ":".join(ip)
        #end if

        return ip
    else:
        return False
    #end if
#end def
        
def getIpv4Range(ip_start, ip_end):
    ip_list = []
    ip_start_int = ipv4Toint(ip_start)
    ip_end_int = ipv4Toint(ip_end)

    if ip_start_int > ip_end_int:
        ip_list = False
    elif ip_start_int == ip_end_int:
        ip_list.append(ip_start)
    else:
        for i in range(ip_start_int, ip_end_int+1):
            ip = intToipv4(i)
            ip_list.append(ip)
        #end for
    #end if

    return ip_list
#end def

def getIpv6Range(ip_start, ip_end):
    ip_list = []
    ip_start = fullIpv6(ip_start)
    ip_end = fullIpv6(ip_end)

    if ip_start == False or ip_end == False:
        return False
    #end if
    if ip_start == ip_end:
        ip_list.append(easyIpv6(ip_start))
        return ip_list
    #end if
    if cmp(ip_start,ip_end) == 1:
        return False
    #end if

    ip_org = ""
    i = 0
    for i in range(len(ip_start)):
        if ip_start[i] != ip_end[i]:
            ip_org = ip_start[0:i]
            ip_start = ip_start[i:]
            ip_end = ip_end[i:]
            break
        #end if
    #end for
    if len(ip_start) > 4:
        return False
    #end if
    j = len(ip_start)

    for i in range(hex2dec(ip_start),hex2dec(ip_end)+1):
        t = dec2hex(i)
        t = "0000%s" % (t)
        t = "%s%s" % (ip_org,t[-j:])
        ip_list.append(easyIpv6(t))
    #end for

    return ip_list
#end def

def domainToip(domain):
    try:
        if domain == "":
            return False
        #end if
        if domain.find("://") > 0:
            domain = domain.split("://")[1]
        #end if
        if checkIpv4(domain) or checkIpv6(domain):
            return domain
        #end if
        match = re.findall(u"((\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5]))",domain,re.I)
        if match and len(match) > 0:
            print match
            return match[0][0]
        #end if

        match = re.findall(u"((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?", domain, re.I)
        if match and len(match) > 0:
            
            return match[0][0]
        #end if

        if domain.find(":") > 0:
            if len(domain.split(":") > 2):
                return False
            else:
                domain = domain.split(":")[0]
            #end if
        #end if

        res = socket.getaddrinfo(domain, None)
        if res and len(res) > 0:
            return res[0][4][0]
        #end if

        return False

    except Exception,e:
        return False
    #end try
#end def

def ipv6ToBin(ipv6):
    try:
        tmp = fullIpv6(ipv6)
        if tmp == False:
            return False
        res_ip = ''
        ret = []
        for i in range(len(tmp)):
            if tmp[i] != ':':
                res = bin(int(tmp[i],16))
                res = res[2:]
                a = len(res)
                if a < 4:
                    r = ''
                    for j in range(4-a):
                        r += '0'
                    res += r
                res_ip += res

        return res_ip

    except Exception, e:
        return False
    #end try
#end def

def getCurrentTimestamp():
    return time.time()
#end def

def getCurrentTimeFormat():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#end def

def timeToFormat(timestamp):
    try:
        timeFormat = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))

        return timeFormat
    except Exception, e:
        raise e
    #end try
#end def

def formatToTime(timeFormat):
    try:
        timeArray = time.strptime(timeFormat, "%Y-%m-%d %H:%M:%S")
        timestamp = time.mktime(timeArray)

        return timestamp
    except Exception, e:
        raise e
    #end try
#end def


def sam(sampleNo, mu, sigma):
    """
        根据正态分布获取列表
        :param sampleNo: 获取数的个数
        :param mu:均值
        :param sigma:标准差

    """
    s = np.random.normal(mu, sigma, sampleNo)
    return s

def sam_simple_po(sampleNo,mu, sigma,max_n,min_n=0):
    """
        根据正态分布和一些限制获取列表，限制为控制最大最小值,最小值默认为0
        :param sampleNo: 获取数的个数
        :param mu:均值
        :param sigma:标准差
        :param sigma:标准差

    """
    s = np.random.normal(mu, sigma, sampleNo)
    ss=[]
    for e in s:
        e=int(e)
        if e<min_n:
            e=min_n
        elif e>max_n:
            e=max_n
        ss.append(e)
    return ss


def po_int(s_list):
    #转化为正整数和0组成的列表
    ss_list=[]
    for e in s_list:
        if e>0:
            ss_list.append(int(e))
        else:
            ss_list.append(0)
    return ss_list


def RandomSampling(dataMat, number):
    # 不放回抽样
    try:
        slice = random.sample(dataMat, number)
        return slice
    except:
        print 'sample larger than population'




def time_ana(date_str,date_length):
    """
    获取造数据的日期列表，得到日期和星期
        :param date_str: 数据的事件的起始日期，时间格式'%Y-%m-%d'
        :param date_length:持续天数

    """
    date_list=[]
    dt=date_str
    dt_line=datetime.datetime(int(dt[0:4]), int(dt[5:7]), int(dt[8:10]))
    for i in xrange(date_length):
        date_elem={}
        t = dt_line + datetime.timedelta(days=i)
        riqi=t.strftime('%Y-%m-%d')
        anyday = datetime.datetime(int(riqi[0:4]), int(riqi[5:7]), int(riqi[8:10])).strftime("%w");
        date_elem["riqi"]=riqi
        date_elem["xinqi"]= anyday
        date_list.append(date_elem)
    return date_list


def list_of_groups(l, s):
    ll=[]
    for ii in range(s):
        ll.append([])
    ss=len(ll)
    for i in range(len(l)):
        n=i%s
        a=ll[n]
        a+=[l[i]]
    return ll