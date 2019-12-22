#!/usr/bin/env python
# encoding: utf8

import sys
from elasticsearch import Elasticsearch
import json

# ip = sys.argv[1]
# index_name = sys.argv[2]#eventaction_20190828v181
#
# es = Elasticsearch([ip],port=9200,timeout=180)
# # print es,"对接成功!"
#
#
# def query_data():
#     res = es.search(index_name)
#     print res
#     total = res['hits']['total']
#     print total
#     return total
#
#
# query_data()

# a='abc'
# print a.find('c')!=1

import json

resBody = '{"key":"a"}'
message = json.loads(resBody)
output =  message['hits']['total']
vars.put("totalCount",output)

import sys
sys.path.append(r'F:\Anaconda3\envs\QZ\Lib\site-packages')
from elasticsearch import Elasticsearch
from __future__ import unicode_literals
import logging

from ..transport import Transport
from ..exceptions import TransportError
from ..compat import string_types, urlparse, unquote
from .indices import IndicesClient
from .ingest import IngestClient
from .cluster import ClusterClient
from .cat import CatClient
from .nodes import NodesClient
from .remote import RemoteClient
from .snapshot import SnapshotClient
from .tasks import TasksClient
from .xpack import XPackClient
from .utils import query_params, _make_path, SKIP_IN_PATH
import json
'''
1.获取接口响应信息，获知返回条数
2.获取对应Es全文索引条数
3.对比判断是否一致
'''
#ip = '192.168.0.64'
#index_name = 'eventaction_20190828v181'
#对接ES
es = Elasticsearch(['192.168.0.64'],9200)

#获取索引文档数
EsRes = es.search('eventaction_20190828v181')
#    print res
EsTotal = EsRes['hits']['total']
print EsTotal


#获取请求响应信息
resBody = prev.getResponseDataAsString()
print resBody
response =  json.loads(resBody)
data = response['data']
totalCount = data['totalCount']
print totalCount


#判断
if resBody.find("\"success\":true")!=-1 and EsTotal==totalCount:
	prev.setSuccessful(true);
	print "模糊搜索list接口接口执行完成！"  + "\r\n" +resBody
elif resBody.find("\"success\":true")!=-1 and EsTotal!=totalCount:
	pre.setSuccessful(false)
else:
	prev.setSuccessful(false)
	print "模糊搜索list接口执行失败！"
#	log.info "模糊搜索list接口发生错误的请求信息：" + prev.getSamplerData() + "\r\n"
#	log.info "模糊搜索list接口发生错误的的响应信息：" + resBody + "\r\n"
	print "模糊搜索list接口发生错误的请求信息：" + prev.getSamplerData()
	print "模糊搜索list接口发生错误的响应信息：" + resBody