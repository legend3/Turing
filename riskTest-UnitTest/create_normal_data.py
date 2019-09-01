#-*-coding:utf8-*-
from __future__ import division
import random
from pykafka import KafkaClient
import numpy as np
import json
import time
import math
import datetime
from lib.common import *




# class Predata():
def get_data(api_list=[],ip_list=[],user_list=[],hour_list=[],start_date="2018-07-01",test_pan=30,hosts="192.168.0.96:9093",topic="ApiEvents",api_top_num=5):



        def get_api_content(url="",tm="",seq=2,user="",ip=""):
            """
                :param tm: 10位时间戳
                :param url: 接口URL
                :param body: 识别主体
                :param user: 用户名表识
                :param ip: ip

            """

            if url=="http://www.cdplatform.com/bss/ncrm/ncustomer/nPanorama/profiling/json/datas.sdo":
                phone = str(1396123) + str(seq+1)
                email="1536501%d@163.com"%(seq)
                card="622700247017028%d"%(seq)
                pid="32048119900410%d"%(seq)
                body={"success": True, "data":{"user": "晓红", "phone": phone, "email": email, "card":card, "pid": pid}}

            elif url=="http://www.cdplatform.com/bss/ncrm/ncustomer/customerListTable/json/getCustomerListData.sdo":
                ddd=[]
                for i in xrange(25):
                    seqq=(1813*i)%1000+10000+seq
                    phone = str(139612)+str(seqq+1)
                    email = "153652%d@qq.com" % (seqq)
                    card = "62270024701702%d" % (seqq)
                    pid = "3204811991041%d" % (seqq)
                    dd={"user": "晓红", "phone": phone, "email": email, "card":card, "pid": pid}
                    ddd.append(dd)
                body = {"success": True, "data": ddd }

            elif url=="http://www.cdplatform.com/bss/ncrm/ncustomer/shop/abroad/html/datas.sdo":
                detailBody = "<!DOCTYPE html>\n<html >\n  <head>\n    <meta charset=\"utf-8\">\n    <title> ShowDoc</title>\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <meta name=\"description\" content=\"\">\n    <meta name=\"author\" content=\"\">\n    <link href=\"/Public/bootstrap/css/bootstrap.min.css\" rel=\"stylesheet\">\n    <link href=\"/Public/css/showdoc.css\" rel=\"stylesheet\">\n      <script type=\"text/javascript\">\n      var DocConfig = {\n          host: window.location.origin,\n          app: \"/index.php?s=/\",\n          server: \"server/index.php?s=\",\n          pubile:\"/Public\",\n      }\n\n      DocConfig.hostUrl = DocConfig.host + \"/\" + DocConfig.app;\n      </script>\n      <script src=\"/Public/js/lang.zh-cn.js?v=212\"></script>\n  </head>\n  <body>\n\n<link rel=\"stylesheet\" href=\"/Public/css/item/index.css?v=1.234\" />\n    <div class=\"container-narrow\">\n\n      <div class=\"masthead\">\n        <div class=\"btn-group pull-right\">\n        <a class=\"btn btn-link\" href=\"https://github.com/star7th/showdoc/issues\" target=\"_blank\">反馈</a>\n        <a class=\"btn btn-link dropdown-toggle\" data-toggle=\"dropdown\" href=\"#\">\n       海外购物        <span class=\"caret\"></span>\n        </a>\n        <ul class=\"dropdown-menu\">\n        <!-- dropdown menu links -->\n          <li><a href=\"/index.php?s=/Home/User/setting\">个人设置</a></li>\n<!--           <li><a href=\"#share-home-modal\"  data-toggle=\"modal\">分享主页</a></li>\n -->      \n          <li><a href=\"/index.php?s=/Home/index/index\">网站首页</a></li>\n          <li><a href=\"/index.php?s=/Home/User/exist\">"
                detailBody += "email:%d@qq.com</a></li>\n\n        </ul>\n        </div>\n\n        </ul>\n        <h3 class=\"muted\"><img src=\"/Public/logo/b_64.png\" style=\"width:50px;height:50px;margin-bottom:15px;\" alt=\"\">ShowDoc</h3>\n      </div>\n\n      <hr>\n\n    <div class=\"container-thumbnails\">\n      <ul class=\"thumbnails\" id=\"item-list\">\n\n      </ul>\n    </div>\n\n\n    </div> <!-- /container -->\n\n<!-- 分享项目框 -->\n<div class=\"modal hide fade\" id=\"share-home-modal\">\n  <div class=\"modal-header\">\n    <button type=\"button\" class=\"close\" data-dismiss=\"modal\" aria-hidden=\"true\">&times;</button>\n  </div>\n  <div class=\"modal-body\">\n    <p>" % (
                1396123 + seq)

                detailBody += "Card:622700247017027%d,Passport:E%d,ID:320111199511210414</p>\n  </div>\n</div>\n\n\n    \n\t<script src=\"/Public/js/beta131common/jquery.min.js\"></script>\n    <script src=\"/Public/bootstrap/js/bootstrap.min.js\"></script>\n    <script src=\"/Public/js/beta131common/showdoc.js?v=1.1\"></script>\n    <script src=\"/Public/layer/layer.js\"></script>\n    <script src=\"/Public/js/dialog.js\"></script>\n    <div style=\"display:none\">\n    \t    </div>\n  </body>\n</html> \n\n <script src=\"/Public/js/item/index.js?v=12\"></script>" % (
                23+seq,87555321 + seq)
                body=detailBody
            else:
                body=""


            api_content= {
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
                                "cookie": "JSESSIONID=E0D68A1F43CEEE040C9E338875FAC501; UserID="+user+"; PortalToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
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
                                "content-type":"application/json"
                            },
                            "body": body,
                            "gzip_flag": 0,
                            "set_cookies_list": [""]
                        }
                    }
            return api_content





        def time_s(RandomSampling,batch_clock,batch_long,power_b,riqi):
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
                m_num=sam_simple_po(1,power_b-4,5,11,1)[0]+1
                for j in xrange(m_num):
                    tem=random.uniform(0, 60)
                    total_stamp=int((clock_stamp[0]+60000*m+tem*1000)/1000)
                    stamp_list.append(total_stamp)
            return stamp_list



        def choice_time_during(hour_list,time_puch=3):
            #根据概率获取3个工作时间段，按频率降序排列
            hour_now_list=[]
            while len(hour_now_list)<time_puch:
                s_p = random.uniform(0, 1)
                if s_p<=0.35:
                    hour_now_list.append(hour_list[0])
                elif s_p<=0.65:
                    hour_now_list.append(hour_list[1])
                elif s_p <= 0.82:
                    hour_now_list.append(hour_list[2])
                elif s_p<=0.92:
                    hour_now_list.append(hour_list[3])
                elif s_p<=0.97:
                    hour_now_list.append(hour_list[4])
                else:
                    hour_now_list.append(hour_list[5])
                hour_now_list=list(set(hour_now_list))
            return hour_now_list




        def ip_distribution(ips,ip_n,num):
            #获取该用户当天的主要IP和备用IP，模拟IP当天的变动
            ip2=ips[1]
            for i in xrange(num):
                if ip_n%num ==i:
                    ip1=ips[i]
                if ip_n%(num+3)==i:
                    ip2=ips[i]
            return ip1,ip2



        client = KafkaClient(hosts=hosts)
        topic = client.topics[topic]
        producer = topic.get_sync_producer()
        time_list = time_ana(start_date, test_pan)
        user_list_ana=[]
        user_power=7
        ii=0
        for i in xrange(len(user_list)):
            #生成用户列表，和该用户对应的IP池子，人均IP最多为8个；
            #生成用户的访问强度
            user_info={}
            user=user_list[i]

            ip6=ip_list[i+1]
            # ip7=ip_list[202-i]
            ip8=ip_list[i+1]
            ips=[ip8,ip6]
            user_power = sam_simple_po(1, 13, 4, 26,1)[0]
            # user_power+=3
            user_info["user"]=user
            user_info["user_power"]=user_power
            user_info["ips"]=ips
            user_list_ana.append(user_info)
            # 生成员工数量基数   每分 基数为16 -4


        ip_ne=0

        for t_e in time_list:
                print t_e
            #遍历日期，考虑周末和工作日，并根据星期生成日期访问强度
                xinqi = int(t_e["xinqi"])
                riqi = t_e["riqi"]
                date_power = 0.35 * math.sqrt(xinqi + 1)

                if xinqi==6 or xinqi==0:
                    user_n_weekend=(xinqi%4)*9+42
                    api_num = sam_simple_po(1, -1, 1, 3,2)[0]
                    user_list_now=RandomSampling(user_list_ana, user_n_weekend)

                else:
                    api_num=sam_simple_po(1, 3.1,0.4,api_top_num,1)[0]

                    user_list_now=user_list_ana
                ip_ne += 1
                aaa = 0

                for ur in user_list_now:
                    user=ur["user"]
                    user_power=ur["user_power"]
                    ips=ur["ips"]
                    #每人每天抽取三个时间段
                    hour_now_list=choice_time_during(hour_list)
                    ip_z=ips[0]
                    ip_c = ips[1]
                    ip_p=random.uniform(0, 1)
                    ip_now=[ip_z]
                    if ip_p<0.2:
                        ip_now=[ip_z,ip_c]
                    #根据用户访问强度和日期访问强度，生成综合访问强度power
                    power=user_power-date_power
                    api_list_now = RandomSampling(api_list, api_num)

                    api_power=0
                    for api in api_list_now:
                        api_power+= 0.2

                        url=api["url"]


                        batch_num=sam_simple_po(1, 1.8,0.4,3,1)[0]

                        #每个接口对应三个时间段
                        batch_time=RandomSampling(hour_now_list, batch_num)
                        flag=False
                        if "login" in url:
                            batch_time=["09:00:00$12:00:00"]
                            flag=True
                        if batch_time:


                            # if len(ip_now)>1:
                            for j in xrange(len(batch_time)):
                                ip_now_e=ip_now[0]

                                if j==len(batch_time)-1 and len(ip_now)>1:

                                    ip_now_e = ip_now[1]
                                # 根据用户访问时间段，对综合访问强度power再修正，体现不同工作时间段的强度变化
                                power_b=(power-2*j)*0.5+api_power
                                # print power_b

                                batch_clock=batch_time[j]

                                batch_long=sam_simple_po(1,12,6,23,2)[0]
                                # print batch_long

                                if flag:
                                    batch_long=1
                                    power_b=-200
                                rr = time_s(RandomSampling, batch_clock, batch_long, power_b, riqi)


                                aaa+=len(rr)
                                for each in rr:
                                    ii+=1
                                    oi=ii%8900+1000
                                    a = get_api_content(url=url, tm=each,seq=oi,ip=ip_now_e,user=user)
                                    # print type(a)
                                    # info=json.dumps(a)
                                    info = json.write(a)
                                    # print info
                                    producer.produce(info)
                # print aaa


    # if __name__ == '__main__':
def pre_data_main(start_date,test_pan,hosts):
           #api_top_num为接口池子最大的数量，接口池子为api_list
           #ip_list IP池子     user_list 用户池子    hour_list 工作时刻池子，按频繁度排序
           #start_date 造数据开始时间   test_pan 数据持续时间，单位为天
            a1 = {"url": "http://www.cdplatform.com/login.do", "body": {}}
            b2={"success": True, "data":{"user": "晓红", "phone": "15365019846", "email": "15365019846@qq.com", "card":"6227002470170278192", "pid": "320481199004101010"}}
            a2={"url":"http://www.cdplatform.com/bss/ncrm/ncustomer/nPanorama/profiling/json/datas.sdo","body":b2}
            b3={"success": True, "data":[{"user": "晓红", "phone": "15365019832", "email": "15365019832@163.com", "card":"6227002470170278192", "pid": "320481199004101010"},{"user": "晓红", "phone": "15365019833", "email": "15365019833@163.com", "card":"6227002470170278192", "pid": "320481199004101010"},{"user": "晓红", "phone": "15365019834", "email": "15365019834@163.com", "card":"6227002470170278192", "pid": "320481199004101010"},{"user": "晓红", "phone": "15365019835", "email": "15365019835@163.com", "card":"6227002470170278192", "pid": "320481199004101010"},{"user": "晓红", "phone": "15365019836", "email": "15365019836@163.com", "card":"6227002470170278192", "pid": "320481199004101010"},{"user": "晓红", "phone": "15365019837", "email": "15365019837@163.com", "card":"6227002470170278192", "pid": "320481199004101010"},{"user": "晓红", "phone": "15365019838", "email": "15365019838@163.com", "card":"6227002470170278192", "pid": "320481199004101010"},{"user": "晓红", "phone": "15365019839", "email": "15365019839@163.com", "card":"6227002470170278192", "pid": "320481199004101010"},{"user": "晓红", "phone": "15365019840", "email": "15365019840@163.com", "card":"6227002470170278192", "pid": "320481199004101010"},{"user": "晓红", "phone": "15365019841", "email": "15365019841@163.com", "card":"6227002470170278192", "pid": "320481199004101010"},{"user": "晓红", "phone": "15365019842", "email": "15365019842@163.com", "card":"6227002470170278192", "pid": "320481199004101010"},{"user": "晓红", "phone": "15365019843", "email": "15365019843@163.com", "card":"6227002470170278192", "pid": "320481199004101010"},{"user": "晓红", "phone": "15365019844", "email": "15365019844@163.com", "card":"6227002470170278192", "pid": "320481199004101010"},{"user": "晓红", "phone": "15365019845", "email": "15365019845@163.com", "card":"6227002470170278192", "pid": "320481199004101010"},{"user": "晓红", "phone": "15365019846", "email": "15365019846@163.com", "card":"6227002470170278192", "pid": "320481199004101010"},{"user": "晓红", "phone": "15365019847", "email": "15365019847@163.com", "card":"6227002470170278192", "pid": "320481199004101010"},{"user": "晓红", "phone": "15365019848", "email": "15365019848@163.com", "card":"6227002470170278192", "pid": "320481199004101010"},{"user": "晓红", "phone": "15365019849", "email": "15365019849@163.com", "card":"6227002470170278192", "pid": "320481199004101010"},{"user": "晓红", "phone": "15365019850", "email": "15365019850@163.com", "card":"6227002470170278192", "pid": "320481199004101010"},{"user": "晓红", "phone": "15365019851", "email": "15365019851@163.com", "card":"6227002470170278192", "pid": "320481199004101010"},{"user": "晓红", "phone": "15365019852", "email": "15365019852@163.com", "card":"6227002470170278192", "pid": "320481199004101010"},{"user": "晓红", "phone": "15365019853", "email": "15365019853@163.com", "card":"6227002470170278192", "pid": "320481199004101010"},{"user": "晓红", "phone": "15365019854", "email": "15365019854@163.com", "card":"6227002470170278192", "pid": "320481199004101010"},{"user": "晓红", "phone": "15365019855", "email": "15365019855@163.com", "card":"6227002470170278192", "pid": "320481199004101010"},{"user": "晓红", "phone": "15365019856", "email": "15365019856@163.com", "card":"6227002470170278192", "pid": "320481199004101010"},{"user": "晓红", "phone": "15365019857", "email": "15365019857@163.com", "card":"6227002470170278192", "pid": "320481199004101010"},{"user": "晓红", "phone": "15365019858", "email": "15365019858@163.com", "card":"6227002470170278192", "pid": "320481199004101010"},{"user": "晓红", "phone": "15365019859", "email": "15365019859@163.com", "card":"6227002470170278192", "pid": "320481199004101010"},{"user": "晓红", "phone": "15365019860", "email": "15365019860@163.com", "card":"6227002470170278192", "pid": "320481199004101010"},{"user": "晓红", "phone": "15365019861", "email": "15365019861@163.com", "card":"6227002470170278192", "pid": "320481199004101010"}]}
            a3={"url":"http://www.cdplatform.com/bss/ncrm/ncustomer/customerListTable/json/getCustomerListData.sdo","body":b3}
            b4="<!DOCTYPE html>\n<html >\n  <head>\n    <meta charset=\"utf-8\">\n    <title> ShowDoc</title>\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <meta name=\"description\" content=\"\">\n    <meta name=\"author\" content=\"\">\n    <link href=\"/Public/bootstrap/css/bootstrap.min.css\" rel=\"stylesheet\">\n    <link href=\"/Public/css/showdoc.css\" rel=\"stylesheet\">\n      <script type=\"text/javascript\">\n      var DocConfig = {\n          host: window.location.origin,\n          app: \"/index.php?s=/\",\n          server: \"server/index.php?s=\",\n          pubile:\"/Public\",\n      }\n\n      DocConfig.hostUrl = DocConfig.host + \"/\" + DocConfig.app;\n      </script>\n      <script src=\"/Public/js/lang.zh-cn.js?v=212\"></script>\n  </head>\n  <body>\n\n<link rel=\"stylesheet\" href=\"/Public/css/item/index.css?v=1.234\" />\n    <div class=\"container-narrow\">\n\n      <div class=\"masthead\">\n        <div class=\"btn-group pull-right\">\n        <a class=\"btn btn-link\" href=\"https://github.com/star7th/showdoc/issues\" target=\"_blank\">反馈</a>\n        <a class=\"btn btn-link dropdown-toggle\" data-toggle=\"dropdown\" href=\"#\">\n       海外购物        <span class=\"caret\"></span>\n        </a>\n        <ul class=\"dropdown-menu\">\n        <!-- dropdown menu links -->\n          <li><a href=\"/index.php?s=/Home/User/setting\">个人设置</a></li>\n<!--           <li><a href=\"#share-home-modal\"  data-toggle=\"modal\">分享主页</a></li>\n -->      \n          <li><a href=\"/index.php?s=/Home/index/index\">网站首页</a></li>\n          <li><a href=\"/index.php?s=/Home/User/exist\">email:8235345@qq.com</a></li>\n\n        </ul>\n        </div>\n\n        </ul>\n        <h3 class=\"muted\"><img src=\"/Public/logo/b_64.png\" style=\"width:50px;height:50px;margin-bottom:15px;\" alt=\"\">ShowDoc</h3>\n      </div>\n\n      <hr>\n\n    <div class=\"container-thumbnails\">\n      <ul class=\"thumbnails\" id=\"item-list\">\n\n      </ul>\n    </div>\n\n\n    </div> <!-- /container -->\n\n<!-- 分享项目框 -->\n<div class=\"modal hide fade\" id=\"share-home-modal\">\n  <div class=\"modal-header\">\n    <button type=\"button\" class=\"close\" data-dismiss=\"modal\" aria-hidden=\"true\">&times;</button>\n  </div>\n  <div class=\"modal-body\">\n    <p>Card:6227002470170278192,Passport:E81879580,ID:320111199511210414</p>\n  </div>\n</div>\n\n\n    \n\t<script src=\"/Public/js/beta131common/jquery.min.js\"></script>\n    <script src=\"/Public/bootstrap/js/bootstrap.min.js\"></script>\n    <script src=\"/Public/js/beta131common/showdoc.js?v=1.1\"></script>\n    <script src=\"/Public/layer/layer.js\"></script>\n    <script src=\"/Public/js/dialog.js\"></script>\n    <div style=\"display:none\">\n    \t    </div>\n  </body>\n</html> \n\n <script src=\"/Public/js/item/index.js?v=12\"></script>"
            a4={"url":"http://www.cdplatform.com/bss/ncrm/ncustomer/shop/abroad/html/datas.sdo","body":b4}
            b5="<buffalo-reply><map><phone>0311-89898959</phone><email>rongsheng@aliyun.com</email><address>河北省石家庄市维明南大街200号</address></map></buffalo-reply>"
            a5={"url":"http://10.2.30.161:8080/bss/ncrm/company/xml/datas.sdo","body":b5}
            api_list=[a1,a2,a3,a4]

            ip_list_t=["192.168.9."+str(i) for i in xrange(2,200)]
            ip_inner=['84.235.122.205', '75.193.225', '75.193.251', '202.100.073.255', '202.101.104.031', '202.101.096.127',
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
            ip_list=ip_list_t+ip_inner
            user_list=['htoedi', 'ayvzyf', 'hvixhx', 'gotbiq', 'ukeqqx', 'hwvuat', 'ewlwrt', 'xxjxzo', 'uibixg', 'qlgwas', 'gbrpfa', 'qgplcx', 'rjvodk', 'siipeo', 'myquzl', 'thwyrq', 'towlik', 'unqzdk', 'qtmvpm', 'zmefsx', 'nhvtmg', 'ztqysq', 'kucgtz', 'regsbx', 'ugfqok', 'cyefuc', 'pagirc', 'xmdupy', 'urhzfi', 'odyzcj', 'youvbt', 'mdllxc', 'bdpppl', 'jxzcdg', 'cdulmn', 'seyvbv', 'ufcvmw', 'ujrsav', 'niqxos', 'excgsh', 'yyvxck', 'xkqlwe', 'uffmip', 'zkinmv', 'dpirju', 'tlchtn', 'wfxipx', 'zzszvy', 'oktgtn', 'qcueut', 'hufzma', 'cqtuco', 'qjaqno', 'qvtqoh', 'ikdqux', 'uocryb', 'qmnaah', 'xvghdc', 'onllzl', 'uuahir', 'rdadkg', 'gwfakc', 'qxdaoh', 'acvtyg', 'hyjksl', 'zbryvu', 'zletbq', 'noowmw', 'wfcbgk', 'wegyle', 'timhgl', 'nozfke', 'lueglj', 'khvcku', 'vzcqhf', 'uptsox', 'vgufoq', 'jevmqt', 'tevmar', 'geggsb', 'lfpbqi', 'wsfluz', 'nkcdoh', 'lqqbiu', 'qztxal', 'fymzqv', 'blpsix', 'pciwpv', 'kfypnp', 'vgsyvt', 'stmzzg', 'teocti', 'jrmhzi', 'jmgtlx', 'hrxbct', 'onfywk', 'pjodll', 'vmpnjg', 'vifihu', 'bjmuan', 'xqvdcx', 'zwucdz', 'lwvluv', 'ypkehk', 'ecwiit', 'kmlzue', 'pxgatz', 'fmvwnd', 'fdahgf', 'zmwpdj', 'wfhkbf', 'tboxpy', 'fcitcu', 'oiswkn', 'mxjmmf', 'mbdalb', 'zgealm', 'paavjt', 'oxezvc', 'vbpuox', 'qsuklu', 'fgiicg', 'ebikiw', 'stftgq', 'hvsjwm', 'loogpz', 'dpdlyz', 'fdjpxv', 'bpebjp', 'msomwz', 'fbftcv', 'jdahqu', 'ggbjlw', 'ypiugj']

            hour_list=["09:00:00$12:00:00","15:00:00$18:00:00","13:00:00$15:00:00","19:00:00$20:00:00","20:00:00$21:00:00","21:00:00$23:00:00"]
            # print len(ip_list)
            #要改的参数只有一个：IP：10.2.130.55
            # print start_date
            # print test_pan
            get_data(api_list,ip_list,user_list,hour_list,start_date=start_date,test_pan=test_pan,hosts = hosts,topic = "ApiEvents",api_top_num=4)