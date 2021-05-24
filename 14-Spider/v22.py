#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2019-12-22 11:35:22
lastTime: 2021-05-25 01:24:22
LastAuthor: Do not edit
FilePath: /Turing/14-Spider/v22.py
Description: 
version: 
'''


'''
使用参数headers和params
研究返回结果

'''

import requests

# 完整访问url是下面url加上参数构成
# url = "http://www.baidu.com/?"
url = "http://d.xzfile.com/down/wannishiwunian_downcc.zip"
# url = "http://192.168.0.64"

kw = {
    "wd": "王八蛋"
    # "username": "webadmin",
    # "password": "webadmin123456",
    # "vcode": "wannengyanzhengma"
}
headers = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",
    "Host": "d.xzfile.com",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Referer": "http://www.downcc.com/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",

}

rsp = requests.get(url, headers=headers)
print(rsp)
# print(rsp.text)#注意：此处需要修改IDE字符编码为UTF-8
# print(rsp.content)
# print(rsp.url)
print(rsp.encoding)
print(rsp.status_code) # 请求返回码
# print(rsp.is_redirect)
# print(rsp.cookies)
# print(rsp.headers)
with open("rsp.content", "w", ) as f:
    f.write()


