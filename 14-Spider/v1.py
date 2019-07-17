'''
python2和python3在导入urlrequest的方式都不一样。

python2是这样：import urllib2

而python3里面把urllib分开了，分成了urlrequest和urlerror，在这里我们只需导入urlrequest即可。from urllib.request import urlopen
'''
from urllib import request
'''
使用urllib.request请求一个网页内容，并把内容打印出来
'''


if __name__ == '__main__':

    url = "http://jobs.zhaopin.com/195435110251173.htm?ssidkey=y&ss=409&ff=03&sg=2644e782b8b143419956320b22910c91&so=1"
    # 打开相应url并把相应页面作为返回
    rsp = request.urlopen(url)#rsp为响应的信息，字节类型

    # 把返回结果读取出来
    # 读取出来内容类型为bytes
    html = rsp.read()
    print(type(html))#字节类型

    # 如果想把bytes内容转换成字符串，需要解码
    html = html.decode("utf-8")
    print(type(html))
    print(html)
