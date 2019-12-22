from urllib import request
import requests
from bs4 import BeautifulSoup
import re

'''
BeautifulSoup结合正则匹配
'''

url = 'http://www.baidu.com'

# rsp = request.urlopen(url)
# content = rsp.read()

headers = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
}

rsp = requests.get(url,headers=headers)
content = rsp.text

#html字节"还原"成html
soup = BeautifulSoup(content, 'lxml')

print("==" * 12)
tags = soup.find_all(re.compile('^me'), content="always")#将content作为搜索tag的属性
for tag in tags:
    print(tag)
print("==" * 12)