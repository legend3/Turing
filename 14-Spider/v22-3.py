import requests

# baseurl = 'http://192.168.0.64/audit-core/login/checkLogin.do'
# data = {
#     "username": "webadmin",
#     "password": "webadmin123456",
#     "vcode": "wannengyanzhengma"
# }
# rsp = requests.post(baseurl,params=data)
# cookiejar = rsp.cookies
# print(type(cookiejar))
# print(cookiejar)
#
# cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
# print(type(cookiedict))
# print(cookiedict)
#
# #同理，json通过loads()转为dict后，获取json中的值
# jsession = cookiedict.get("JSESSIONID")
# print(jsession)

'''
跨请求，传递cookie
'''

# 创建一个session对象，可以保存cookie值(整个项目之后都可以用session访问(保存了cookie))
session = requests.session()

url = "http://192.168.0.156"

url_login = url + "/audit-core/login/checkLogin.do"
url_Analize = url + "/audit-core/fullTextRetrieval/analyze.do"


# 登录
data_login = {
    "username": "webadmin",
    "password": "webadmin123456",
    "vcode": "wannengyanzhengma"
}
Login = session.post(url_login,params=data_login)
print(Login.status_code)
print(Login.json())  # 响应信息

# analize.do
data_Analize = {
    "text": ""
}
Analize = session.post(url_Analize, params=data_Analize)
print(Analize.status_code)
print(Analize.json())  # 响应信息

# label list


'''
关闭SSL（关闭提示）
'''


# rsp = requests.get("https://www.baidu.com",verify=False)
