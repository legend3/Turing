
from urllib import request

# 导入pythopn ssl处理模块
import ssl

'''
去除CA提示
'''
# 利用非认证上下文环境替换认证的向下文环境
ssl._create_default_https_context = ssl._create_unverified_context#去除安全提示

url = "https://www.12306.cn/mormhweb/"
rsp = request.urlopen(url)

html = rsp.read().decode()

print(html)