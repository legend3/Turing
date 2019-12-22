'''
使用参数headers和params
研究返回结果

'''

import requests

# 完整访问url是下面url加上参数构成
url = "http://www.baidu.com/s?"
# url = "http://192.168.0.64"
kw = {
    "wd": "王八蛋"
    # "username": "webadmin",
    # "password": "webadmin123456",
    # "vcode": "wannengyanzhengma"
}
headers = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
}

rsp = requests.get(url, params=kw, headers=headers )
print(rsp)
print(rsp.text)#注意：此处需要修改IDE字符编码为UTF-8
print(rsp.content)
print(rsp.url)
print(rsp.encoding)
print(rsp.status_code) # 请求返回码
print(rsp.is_redirect)




