#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2020-06-21 00:26:42
@lastTime: 2020-06-21 04:22:55
@LastAuthor: Do not edit
@FilePath: \Turing\14-Spider\v22-5 packaging-requests.py
@Description: 
@version: 
'''


import requests
import json

class Rman():
    def __init__(self, method, url, headers, data=None):
        self.res = self.run(method, url, headers, data)

    def post(self, url, headers, data):
        res = requests.post(url=url, headers=headers, data=data).json()
        return json.dumps(res, indent=2, sort_keys=True)
        
    def get(self, url, headers, data):
        res = requests.get(url=url, headers=headers, data=data).json()
        return json.dumps(res, indent=2, sort_keys=True)
    
    def run(self, method, url, headers, data=None):
        res = None
        if method == 'GET':
            res = self.get(url, headers, data)
        elif method == 'POST':
            res = self.post(self, url, headers, data)
        return res
        

if __name__ == '__main__':
    url = "http://www.baidu.com"
    headers = {
        'Content-Length': "208"
    }
    data = {
        'q': 'python', 'cat': '1001'
    }
    res = Rman('GET', url, headers, data)
    print(res)
