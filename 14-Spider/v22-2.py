import requests

# 用户验证
proxy = {"http":"China:123456@:44444"}
requests.get("https://www.baidu.com",proxies=proxy)

# web客户端验证
auth = {"test1":"123456"}#校验信息
rsp = requests.get("http://www.baidu.com",auth=auth)